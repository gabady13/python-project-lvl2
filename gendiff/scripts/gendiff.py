#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='file first')
parser.add_argument('second_file', type=str, help='file second')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def main():
    """Main function."""


if __name__ == '__main__':
    main()
