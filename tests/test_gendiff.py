from os import path
import pytest
from gendiff.gendiff import generate_diff
import json

CURRENT_DIR = path.dirname(__file__)
PLAIN_JSON_DIR = 'plain_json'
PLAIN_YML_DIR = 'plain_yaml'
NESTED_JSON_DIR = 'nested_json'
NESTED_YML_DIR = 'nested_yml'


def path_current(*paths):
    return path.join(CURRENT_DIR, 'fixtures', *paths)


SET_TESTING_DATA = [
    (PLAIN_JSON_DIR, 'original.json', 'modified.json',
     'styl_plain_result.txt', 'stylish'),
    (PLAIN_YML_DIR, 'original.yml', 'modified.yml',
     'styl_plain_result.txt', 'stylish'),
    (NESTED_JSON_DIR, 'original.json', 'modified.json',
     'styl_nested_result.txt', 'stylish'),
    (NESTED_YML_DIR, 'original.yml', 'modified.yml',
     'styl_nested_result.txt', 'stylish'),
    (NESTED_JSON_DIR, 'original.json', 'modified.json',
     'plain_result.txt', 'plain')]


@pytest.mark.parametrize(
    'files_dir, path_origin, path_modified, path_diff, out_format',
    SET_TESTING_DATA)
def test_gendiff(files_dir, path_origin, path_modified, path_diff,
                 out_format):
    res = generate_diff(path_current(files_dir, path_origin),
                        path_current(files_dir, path_modified),
                        out_format)
    diff = open(path_current(path_diff)).read()
    assert res == diff


def test_gendiff_unknown_format():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'original.json'),
            path_current(PLAIN_JSON_DIR, 'modified.json'),
            'unknown_format')


def test_gendiff_skipped_one_file():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'original.json'),
            '')


def test_gendiff_empty_file():
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'original.json'),
            path_current('clean_file.json'))
    with pytest.raises(ValueError):
        assert generate_diff(
            path_current(PLAIN_JSON_DIR, 'original.json'),
            path_current('clean_file.yml'))


def test_format_json():
    res = generate_diff(path_current(NESTED_JSON_DIR, 'original.json'),
                        path_current(NESTED_JSON_DIR, 'modified.json'),
                        'json')
    j1 = json.loads(res)
    j2 = json.load(open(path_current('json_result.json')))
    assert j1 == j2
