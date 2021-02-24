from gendiff.difference import generate_diff
from gendiff.files import read_file


# Test files
FILE1 = 'tests/fixtures/filepath1.json'
FILE2 = 'tests/fixtures/filepath2.json'


# Answer files
ANSWER = 'tests/fixtures/answer.txt'


TEST_DATA = [
    (FILE1, FILE2, ANSWER)
]


def read_txt(path_to_file):
    with open(path_to_file, "r") as answer:
        expected = answer.read()
    return expected.strip()


def test_txt():
    for (file1, file2, answer) in TEST_DATA:
        file_one = read_file(file1)
        file_two = read_file(file2)
        expected = read_txt(answer)
        result = generate_diff(file_one, file_two)
        assert str(result) == expected
