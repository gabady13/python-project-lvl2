import gendiff.constants as const

DESCR_TEMPLATE = {
    const.STATUS_CHANGE: 'was updated. From {_DEL_} to {_NEW_}',
    const.STATUS_DEL: 'was removed',
    const.STATUS_NEW: 'was added with value: {_NEW_}'}


def get_plain(diff):
    plain = diff_to_list(diff, '')
    res = '\n'.join(plain)
    return res


def diff_to_list(diff, prefix=''):
    res = []
    new_prefix = get_new_prefix(prefix, diff[const.KEY_KEY])
    if const.KEY_CHILDREN not in diff:
        values_to_string = {k: to_string(v) for k, v in
                            diff[const.KEY_VALUE].items()}

        descr = DESCR_TEMPLATE.get(diff[const.KEY_TYPE],
                                   '').format(**values_to_string)
        return ['{}\'{}\' {}'.format('Property ', new_prefix, descr)]

    children = filter(lambda key_descr: const.STATUS_STAY != key_descr.get(
        const.KEY_TYPE, None), diff[const.KEY_CHILDREN])
    for child in children:
        res += diff_to_list(child, new_prefix)
    res.sort()
    return res


def get_new_prefix(prefix, key):
    if not prefix:
        return key
    return '{}.{}'.format(prefix, key)


def to_string(value):
    if isinstance(value, dict):
        res = '[complex value]'
    elif isinstance(value, str):
        res = '\'{}\''.format(value)
    elif value is True or value is False or value is None:
        res = {True: 'true', False: 'false', None: 'null'}[value]
    else:
        res = value
    return res
