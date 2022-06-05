import json
import yaml


def parse_json(data):
    return json.loads(data)


def parse_yaml(data):
    return yaml.safe_load(data)


def get_parser(format):
    if 'json' in format:
        parser = parse_json
    elif 'yml' in format\
            or 'yaml' in format:
        parser = parse_yaml
    else:
        raise ValueError('can\'t detect format for: {}'.format(format))
    return parser
