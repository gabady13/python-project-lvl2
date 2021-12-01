#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parsers import parse_args


def main():
    """Print diff between two files."""

    print(generate_diff(parse_args.first_file,
                        parse_args.second_file,
                        parse_args.format))


if __name__ == '__main__':
    main()
