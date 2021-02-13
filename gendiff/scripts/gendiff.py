#!/usr/bin/env python
from gendiff.difference import generate_diff
from gendiff.files import read_file
import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='file first')
parser.add_argument('second_file', type=str, help='file second')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def main():
    """Main function."""
    try:
        first_file = read_file(args.first_file)
        second_file = read_file(args.second_file)
        difference = generate_diff(first_file, second_file)
        print(difference)
    except AttributeError:
        print('You entered unsupported file format')


if __name__ == '__main__':
    main()
