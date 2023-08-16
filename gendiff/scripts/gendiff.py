#!/usr/bin/env python3#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.cli import cli
# import argparse


def main():
    # parser = argparse.ArgumentParser(description='Compares two configuration '
    #                                  ' files and shows a difference.')
    # parser.add_argument('first_file', type=str)
    # parser.add_argument('second_file', type=str)
    # parser.add_argument('-f', '--format',
    #                     type=str, help='set format of output',
    #                     default='stylish')
    # args = parser.parse_args()
    args = cli()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
