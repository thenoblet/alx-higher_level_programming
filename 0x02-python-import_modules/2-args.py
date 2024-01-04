#!/usr/bin/python3

from sys import argv


def main():
    """
    Description: code prints the number of CLI arguments
    """

    # Find no. of CLI arguments without the filename/argv[0]
    arg_len = len(argv[1:])

    """
    Print a formatted string indicating the number of arguments
    and whether they are singular or plural.
        - The format uses a ternary conditional expression
        to handle different cases.
    """
    print("{} argument{}".format(
        arg_len,
        's.' if arg_len == 0 else ':' if arg_len == 1 else 's:'
    ))

    for index, argument in enumerate(argv[1:], start=1):
        print("{}: {}".format(index, argument))


if __name__ == "__main__":
    main()
