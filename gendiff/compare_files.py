
from gendiff.parsers import JSON_FORMAT, YAML_FORMAT


def open_file(file_path):
    """
    Load file from file system
    """

    if '.json' in file_path:
        return open(file_path), JSON_FORMAT
    elif '.yml' in file_path:
        return open(file_path), YAML_FORMAT
    else:
        return None
