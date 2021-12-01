#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parsers import parse_args


def main():
    """Print diff between two files."""
    arg = parse_args()
    print(generate_diff(arg.first_file,
                        arg.second_file,
                        arg.format))


if __name__ == '__main__':
    main()
