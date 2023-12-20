#!/usr/bin/python3
"""Modul for working nodes"""


class Node:
    """A class representing a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in
        the linked list.

    Raises:
        TypeError: If the provided data or next_node is invalid.
    """

    def __init__(self, data, next_node=None):
        """Initialize a node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node.
            Defaults to None.

        Raises:
            TypeError: If the provided data is not an integer or if the
            next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If the provided next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class representing a singly linked list.

    Attributes:
        head: The first node of the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the
        linked list (in increasing order).

        Args:
            value (int): The value to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
