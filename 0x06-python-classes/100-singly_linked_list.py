#!/usr/bin/python3

"""A Python implementation of Singly Linked Lists"""


class Node:
    """Blueprint for the node"""

    def __init__(self, data, next_node=None):
        """
        Creates a new node

        Args:
            data (int): the data integer value to store
            next_node (Node, optional): reference to the next node.
            Defaults to None.

        Raises:
            TypeError: when the data given is an integer or when an invalid
            object is received as the next_node

        Returns:
            Node: an instance of the Node class
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data part of a node

        Returns:
            int: the value stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
         """Sets or updates the data part of a node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node

        Returns:
            Node: reference to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets or updates the reference to the next node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A Singly Linked List Implementation"""

    def __init__(self):
        """Initializes the Linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a node into a linked list while keeping it sorted in
        ascending order

        Args:
            value (int): the integer value to insert
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            new.next_node = temp.next_node
            while temp.next_node and value > temp.next_node.data:
                new.next_node = temp.next_node.next_node
                temp = temp.next_node
            temp.next_node = new

    def __str__(self):
        """
        Returns all data part of Node type in a linked list

        Returns:
            str: the data part of all nodes in a linked list
        """
        res = ""
        temp = self.__head
        while temp is not None:
            res = res + str(temp.data) + "\n"
            temp = temp.next_node
        res = res[:-1]
        return res
