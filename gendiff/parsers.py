import json
import yaml


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def get_data(file_path):
    reader = get_file_reader(file_path)
    with open(file_path, mode='r') as opened_file:
        data = opened_file.read()
    if not data:
        raise ValueError('Files is empty!')

    return reader(data)


def get_file_reader(file_path):
    if '.json' in file_path:
        parser = parse_json
    elif '.yml' in file_path:
        parser = parse_yaml
    else:
        raise ValueError('can\'t detect format for: {}'.format(file_path))
    return parser
