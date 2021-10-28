from os import path
from gendiff.gendiff import generate_diff

FIXTURES_DIR_6 = 'fixtures/step6'


def test_gendiff_json():
    current_dir = path.dirname(__file__)
    path_origin = path.join(current_dir, FIXTURES_DIR_6, 'original.json')
    path_modified = path.join(current_dir, FIXTURES_DIR_6, 'modified.json')
    path_should_be = path.join(current_dir, FIXTURES_DIR_6, 'should_be.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


def test_gendiff_yaml():
    current_dir = path.dirname(__file__)
    path_origin = path.join(current_dir, FIXTURES_DIR_6, 'original.yml')
    path_modified = path.join(current_dir, FIXTURES_DIR_6, 'modified.yml')
    path_should_be = path.join(current_dir, FIXTURES_DIR_6, 'should_be.txt')
    res = generate_diff(path_origin, path_modified)
    should_be = open(path_should_be).read()
    assert res == should_be


if __name__ == '__main__':
    test_gendiff_json()
    test_gendiff_yaml()
