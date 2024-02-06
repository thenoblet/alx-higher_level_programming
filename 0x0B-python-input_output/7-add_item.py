#!/usr/bin/python3

"""
This script provides functionality to save items to a JSON file.
"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def save_to_json_file(args, json_file: str = "add_item.json"):
    """
    Saves items to a JSON file.

    Parameters:
    - args (List[str]): List of items to be saved to the JSON file.
    - json_file (str): The name of the JSON file. Default is "add_item.json".

    Returns:
    None
    """
    new_list = []

    try:
        new_list = load_from_json_file(json_file)
    except Exception:
        save_to_json_file([], json_file)

    for arg in args:
        new_list.append(arg)

    save_to_json_file(new_list, json_file)


if __name__ == "__main__":
    save_to_json_file(sys.argv[1:])
