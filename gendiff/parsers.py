import json
import yaml


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def parse(data, format):
    if 'json' in format:
        parser = parse_json(data)
    elif 'yml' in format\
            or 'yaml' in format:
        parser = parse_yaml(data)
    else:
        raise ValueError('can\'t detect format for: {}'.format(format))
    return parser
