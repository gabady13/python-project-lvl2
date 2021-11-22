import gendiff.reading as reading
import gendiff.parsers as parsers
import gendiff.constants as const


from gendiff.formatters.make_format import format_diff  # noqa: E402


def generate_diff(file_old, file_new, out_format='stylish'):
    data_old = get_data(file_old)
    data_new = get_data(file_new)
    return format_diff(get_inner_diff(data_old, data_new), out_format)


def get_data(source):
    parser = get_parser(source)
    return parser(reading.read_file(source))


def get_inner_diff(old_data, new_data, root_key=''):
    children = []
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    for key in new_keys - old_keys:
        children.append({const.KEY_KEY: key,
                         const.KEY_STATUS: const.STATUS_NEW,
                         const.KEY_VALUE:
                             {const.VALUE_NEW: new_data.get(key)}})
    for key in old_keys - new_keys:
        children.append({const.KEY_KEY: key,
                         const.KEY_STATUS: const.STATUS_DEL,
                         const.KEY_VALUE:
                             {const.VALUE_DEL: old_data.get(key)}})
    for key in old_keys & new_keys:
        if isinstance(old_data.get(key), dict) \
                and isinstance(new_data.get(key), dict):
            children.append(get_inner_diff(old_data.get(key),
                                           new_data.get(key), key))
        else:
            if old_data.get(key) == new_data.get(key):
                children.append({const.KEY_KEY: key,
                                 const.KEY_STATUS: const.STATUS_STAY,
                                 const.KEY_VALUE:
                                     {const.VALUE_STAY: old_data.get(key)}})
            else:
                children.append({const.KEY_KEY: key,
                                 const.KEY_STATUS: const.STATUS_CHANGE,
                                 const.KEY_VALUE:
                                     {const.VALUE_DEL: old_data.get(key),
                                      const.VALUE_NEW: new_data.get(key)}})

        children.sort(key=get_key)

    res = {const.KEY_KEY: root_key,
           const.KEY_CHILDREN: children}
    return res


def get_key(inner_diff):
    return inner_diff[const.KEY_KEY]


def get_parser(file_path):
    if '.json' in file_path:
        parser = parsers.parse_json
    elif '.yml' in file_path:
        parser = parsers.parse_yaml
    else:
        raise ValueError('can\'t detect format for: {}'.format(file_path))
    return parser
