from operator import itemgetter
import gendiff.constants as const


def get_stylish(diff):
    list_data = stylish_to_list(diff_to_uniform_dict(diff))
    res = '{}\n{}\n{}'.format('{', '\n'.join(list_data), '}')
    return res


def diff_to_uniform_dict(diff):
    res = {}
    current_key = diff[const.KEY_KEY]

    if const.KEY_CHILDREN not in diff:
        for status, value in diff[const.KEY_VALUE].items():
            res[status, current_key] = value
        return res

    for child in diff[const.KEY_CHILDREN]:
        res.update(diff_to_uniform_dict(child))

    if current_key:
        res = {(const.VALUE_STAY, current_key): res}
    return res


def stylish_to_list(data, level=2):
    res = []
    shift = ' ' * level
    sorted_keys = sorted(list(data.keys()), key=itemgetter(1))
    for key in sorted_keys:
        value = data[key]
        formatted_key = format_key(key)
        if isinstance(value, dict):
            res.append('{}{}: {}'.format(shift, formatted_key, '{'))
            res = res + stylish_to_list(value, level + 4)
            res.append('{}  {}'.format(shift, '}'))
        else:
            formatted_value = to_string(value)
            res.append('{}{}:{}'.format(shift, formatted_key, formatted_value))
    return res


def format_key(key):
    if isinstance(key, tuple):
        sign = {const.VALUE_DEL: '-',
                const.VALUE_NEW: '+',
                const.VALUE_STAY: ' '}[key[0]]

        key_single = key[1]
    else:
        sign = ' '
        key_single = key
    return '{} {}'.format(sign, key_single)


def to_string(value):
    shift = ' '
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return '{}{}'.format(shift, value)
