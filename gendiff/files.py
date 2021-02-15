import os.path
import json


def read_file(file):
    abs_path = os.path.abspath(file)
    _, extension = os.path.splitext(abs_path)
    result = ''
    with open(abs_path, 'r') as file_descriptor:
        if extension == '.json':
            result = json.load(file_descriptor)
    return result
