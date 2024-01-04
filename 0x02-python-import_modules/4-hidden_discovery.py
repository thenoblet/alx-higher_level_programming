#!/usr/bin/python3

import hidden_4

"""
Description: Program gets the names defined by the module `hidden_4`
and prints the ones that does not start with an underscore
"""


def main():
    """
    Get the names of all items in the hidden_4 module
    using the `dir` function.
    """
    name = dir(hidden_4)

    # Iterate over the names & print those that don't start with an underscore
    for item in name:
        if not item.startswith('_'):
            print("{}".format(item))


if __name__ == "__main__":
    main()
