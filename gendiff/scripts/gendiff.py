#!/usr/bin/env python3

import argparse
import pathlib
from gendiff.generate_difference import generate_diff


def parsing():
    parser = argparse.ArgumentParser(description='Generate diff',
                                     conflict_handler='resolve')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format', default='stylish', metavar='FORMAT',
                        help='set format of output (default: stylish)')

    args = parser.parse_args()
    return args


def main():
    args = parsing()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
