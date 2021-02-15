REMOVED, ADDED, NON_CHANGED = (
    '-', '+', ''
)


def format_key(key, form):
    return '{} {}'.format(form, key)


def generate_diff(first_file, second_file):
    result = {}
    for key in sorted(first_file.keys() - second_file.keys()):
        result[format_key(key, REMOVED)] = first_file[key]
    for key in sorted(first_file.keys() & second_file.keys()):
        if first_file[key] == second_file[key]:
            result[format_key(key, NON_CHANGED)] = first_file[key]
        else:
            result[format_key(key, REMOVED)] = first_file[key]
            result[format_key(key, ADDED)] = second_file[key]
    for key in sorted(second_file.keys() - first_file.keys()):
        result[format_key(key, ADDED)] = second_file[key]
    return result
