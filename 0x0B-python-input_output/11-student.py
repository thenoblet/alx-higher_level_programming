#!/usr/bin/python3
"""
This module contains the class Student.
"""


class Student:
    """
    Class that defines a student.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - __init__(self, first_name, last_name, age): Initializes a
    new Student object.
    - to_json(self, attrs=None): Returns the dict. representation of a class.
    - reload_from_json(self, json): Replaces the attributes of the
    class from a JSON.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.

        Returns:
        None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a class.

        Parameters:
        - attrs (list): List of attributes to include in the dictionary.
        Default is None.

        Returns:
        dict: Dictionary representation of the class.
        """
        if type(attrs) is not list:
            return self.__dict__
        ans = dict()
        for elem in attrs:
            if type(elem) is not str:
                return self.__dict__
            if elem in self.__dict__.keys():
                ans[elem] = self.__dict__[elem]
        return ans

    def reload_from_json(self, json):
        """
        Replaces the attributes on a class from a JSON.

        Parameters:
        - json (dict): Dictionary containing attribute-value pairs.

        Returns:
        None
        """
        for key, val in json.items():
            if key in self.__dict__.keys():
                self.__dict__[key] = val
