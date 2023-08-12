#!/usr/bin/env python3#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import cli


def main():
    first_file, second_file, format = cli()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
