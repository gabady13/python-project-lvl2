from gendiff.difference import generate_diff
from gendiff.files import read_file


# Test files
FILE1 = "gendiff/tests/fixtures/filepath1.json"
FILE2 = "gendiff/tests/fixtures/filepath2.json"


# Answer files
ANSWER = "gendiff/tests/fixtures/answer.txt"

TEST_DATA = [
    (FILE1, FILE2, ANSWER)
]


def read_txt(path_to_file):
    with open(path_to_file, "r") as answer:
        expected = answer.read()
    return expected.strip()


def test():
    for (file1, file2, answer) in TEST_DATA:
        file_one = read_file(file1)
        file_two = read_file(file2)
        expected = read_txt(answer)
        result = generate_diff(file_one, file_two)
        print(result)
        assert str(result) == expected
