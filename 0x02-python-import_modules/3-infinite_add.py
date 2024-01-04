#!/usr/bin/python3

from sys import argv

"""
Description: program prints the sum of all the integer
values of the command-line arguments
"""


def main():
    result = 0
    for index, argument in enumerate(argv[1:], start=1):
        result += int(argument)

    print(result)


if __name__ == "__main__":
    main()
