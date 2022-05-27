#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format',
                        metavar='FORMAT',
                        help='set format of output',
                        default='stylish')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()


def main():
    """Print diff between two files."""
    arg = parse_args()
    print(generate_diff(arg.first_file,
                        arg.second_file,
                        arg.format))


if __name__ == '__main__':
    main()
