#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parsers import args


def main():
    """Print diff between two files."""
    arg = args
    print(generate_diff(arg.first_file,
                        arg.second_file,
                        arg.format))


if __name__ == '__main__':
    main()
