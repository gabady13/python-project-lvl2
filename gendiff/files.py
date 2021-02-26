import os.path
import json
import yaml

FORMATS = {
    "json": ".json",
    "yml": ".yml",
    "yaml": ".yaml"
}


def read_file(file):
    abs_path = os.path.abspath(file)
    _, extension = os.path.splitext(abs_path)
    result = ''
    with open(abs_path) as file_descriptor:
        if extension == FORMATS["json"]:
            return json.load(file_descriptor)
        if extension == FORMATS["yml"] or format == FORMATS["yaml"]:
            part = yaml.safe_load(file_descriptor)
            return part
    return result
