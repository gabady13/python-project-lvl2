#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parsers import args


def main():
    """Print diff between two files."""
    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))


if __name__ == '__main__':
    main()
