from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def format_diff(inner_diff, out_format):
    if out_format == 'stylish':
        return get_stylish(inner_diff)
    elif out_format == 'plain':
        return get_plain(inner_diff)
    elif out_format == 'json':
        return get_json(inner_diff)
    else:
        raise ValueError('{} is unknown format'.format(out_format))
