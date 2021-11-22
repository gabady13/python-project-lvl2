import gendiff.reading as reading
import gendiff.parsers as parsers
import gendiff.constants as const


from gendiff.formatters.make_format import format_diff  # noqa: E402


def generate_diff(file_old, file_new, out_format='stylish'):
    data_old = get_data(file_old)
    data_new = get_data(file_new)

    inner_diff = get_inner_diff(data_old, data_new)
    diff = format_diff(inner_diff, out_format)

    return diff


def get_data(source):
    parser = get_parser(source)
    return parser(reading.read_file(source))


def get_inner_diff(old_data, new_data, root_key=''):
    children = []
    keys = list(set(old_data.keys()) | set(new_data.keys()))
    for key in sorted(keys):
        if old_data.get(key) is None:
            children.append({const.KEY_KEY: key,
                            const.KEY_STATUS: const.STATUS_NEW,
                            const.KEY_VALUE:
                                {const.VALUE_NEW: new_data.get(key)}})
        elif new_data.get(key) is None:
            children.append({const.KEY_KEY: key,
                             const.KEY_STATUS: const.STATUS_DEL,
                             const.KEY_VALUE:
                                 {const.VALUE_DEL: old_data.get(key)}})
        elif isinstance(old_data.get(key), dict) \
                and isinstance(new_data.get(key), dict):
            stay_key = get_inner_diff(old_data.get(key), new_data.get(key), key)
        else:
            stay_key = {const.KEY_KEY: key}
            if old_data.get(key) == new_data.get(key):
                stay_key.update({const.KEY_STATUS: const.STATUS_STAY,
                                 const.KEY_VALUE:
                                     {const.VALUE_STAY: old_data[key]}})
            else:
                stay_key.update({const.KEY_STATUS: const.STATUS_CHANGE,
                                 const.KEY_VALUE:
                                     {const.VALUE_DEL: old_data.get(key),
                                      const.VALUE_NEW: new_data.get(key)}})
            children.append(stay_key)
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
