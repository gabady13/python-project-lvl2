import os.path
import json


def read_file(file):
    file = os. path.abspath(file)
    file_format = os.path.splitext(file)
    file_format = file_format[1].lower()
    result = ''
    if file_format == '.json':
        result = json.load(open(file))
    return result
