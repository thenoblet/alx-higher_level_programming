#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    # Checking the number of command-line arguments
    arg_len = len(argv[1:])
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # map operators to corresponding functions
    operator_functions = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
    }

    # Parse command line arguments
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    """
    Check if the operator is in the dictionary and
    call the corresponding function from the dictionary
    to perform the operation
    """
    if operator in operator_functions:
        result = operator_functions[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
