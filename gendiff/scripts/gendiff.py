#!/usr/bin/env python3

import argparse

from gendiff.generate_difference import generate_diff
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=Path)
    parser.add_argument('second_file', type=Path)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
