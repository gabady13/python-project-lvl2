import gendiff.parsers as parser
import gendiff.constants as const


from gendiff.formatters.make_format import format_diff  # noqa: E402


def generate_diff(file_path1, file_path2, out_format='stylish'):
    data_path1 = parser.get_data(file_path1)
    data_path2 = parser.get_data(file_path2)

    return format_diff(build_diff(data_path1, data_path2), out_format)


def build_diff(old_data, new_data, root_key=''):
    children = []
    all_keys = sorted(old_data.keys() | new_data.keys())

    for key in all_keys:
        value1 = old_data.get(key)
        value2 = new_data.get(key)
        if value1 == value2:
            children.append({const.KEY_KEY: key,
                             const.KEY_STATUS: const.STATUS_STAY,
                             const.KEY_VALUE:
                                 {const.VALUE_STAY: value1}})
        elif key not in old_data:
            children.append({const.KEY_KEY: key,
                             const.KEY_STATUS: const.STATUS_NEW,
                             const.KEY_VALUE:
                                 {const.VALUE_NEW: value2}})
        elif key not in new_data:
            children.append({const.KEY_KEY: key,
                             const.KEY_STATUS: const.STATUS_DEL,
                             const.KEY_VALUE:
                                 {const.VALUE_DEL: value1}})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            children.append(build_diff(value1, value2, key))
        else:
            children.append({const.KEY_KEY: key,
                             const.KEY_STATUS: const.STATUS_CHANGE,
                             const.KEY_VALUE:
                                 {const.VALUE_DEL: old_data.get(key),
                                  const.VALUE_NEW: new_data.get(key)}})
    res = {const.KEY_KEY: root_key,
           const.KEY_CHILDREN: children}
    return res


def get_key(inner_diff):
    return inner_diff[const.KEY_KEY]
