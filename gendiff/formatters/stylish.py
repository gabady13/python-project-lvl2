import gendiff.constants as const


def get_stylish(diff):
    return '{}\n{}\n{}'.format('{', '\n'.
                               join(stylish_to_list(diff)), '}')


def stylish_to_list(data, level=1):  # noqa:C901
    res = []
    count_space = 2 if level == 1 else 2 + (level - 1) * 4
    shift = ' ' * count_space
    current_key = data[const.KEY_KEY]

    if const.KEY_CHILDREN not in data:
        for status, value in data[const.KEY_VALUE].items():
            key_format = format_key(current_key, status)
            if isinstance(value, dict):
                res.append('{}{}: {}'.
                           format(shift, key_format, '{'))
                res = res + stylish_dict(value, level + 1)
                res.append('{}  {}'.format(shift, '}'))
            else:
                formatted_value = to_string(value)
                res.append('{}{}:{}'.
                           format(shift, key_format, formatted_value))
        return res

    if current_key:
        res.append('{}{}: {}'.format(shift, format_key(current_key), '{'))
        for child in data[const.KEY_CHILDREN]:
            res = res + stylish_to_list(child, level + 1)
        res.append('{}  {}'.format(shift, '}'))
    else:
        for child in data[const.KEY_CHILDREN]:
            res = res + stylish_to_list(child, level)

    return res


def format_key(key, status=''):
    if status:
        sign = {const.VALUE_DEL: '-',
                const.VALUE_NEW: '+',
                const.VALUE_STAY: ' '}[status]
        key_single = key
    else:
        sign = ' '
        key_single = key
    return '{} {}'.format(sign, key_single)


def stylish_dict(data, level):
    res = []
    count_space = 2 if level == 1 else 2 + (level - 1) * 4
    shift = ' ' * count_space

    for key, value in data.items():
        if isinstance(value, dict):
            res.append('{}{}: {}'.format(shift, format_key(key), '{'))
            res = res + stylish_dict(value, level + 1)
            res.append('{}  {}'.format(shift, '}'))
        else:
            formatted_value = to_string(value)
            res.append('{}{}:{}'.format(shift, format_key(key),
                                        formatted_value))

    return res


def to_string(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return ' {}'.format(value)
