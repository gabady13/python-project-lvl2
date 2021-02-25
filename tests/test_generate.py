from gendiff.difference import generate_diff
from gendiff.files import read_file


# Test files
FILE1 = 'tests/fixtures/filepath1.json'
FILE2 = 'tests/fixtures/filepath2.json'
FILE3 = 'tests/fixtures/filepath1.yml'
FILE4 = 'tests/fixtures/filepath2.yml'


# Answer files
ANSWER = 'tests/fixtures/answer.txt'


TEST_DATA_JSON = [
    (FILE1, FILE2, ANSWER)
]

TEST_DATA_YAML = [
    (FILE3, FILE4, ANSWER)
]


def read_txt(path_to_file):
    with open(path_to_file, "r") as answer:
        expected = answer.read()
    return expected.strip()


def test_json():
    for (file1, file2, answer) in TEST_DATA_JSON:
        file_one = read_file(file1)
        file_two = read_file(file2)
        expected = read_txt(answer)
        result = str(generate_diff(file_one, file_two))
        assert result == expected


def test_yaml():
    for (file1, file2, answer) in TEST_DATA_YAML:
        file_one = read_file(file1)
        file_two = read_file(file2)
        expected = read_txt(answer)
        result = str(generate_diff(file_one, file_two))
        assert result == expected
