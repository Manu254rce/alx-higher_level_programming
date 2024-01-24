#!/usr/bin/python3
"""
This are two Python classes
"""


class Node:
    """
    This class contains five functions for defining a node
    element for a single linked list
    """
    def __init__(self, data, next_node=None):
        """
        This function instantiates a node class with a data
        and node pointer attribute

        Args:
            data(int): the integer value to be stored in the node
            next_node(NodeObject): a pointer to the next node in
            the list
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """
        This is a getter function for the data
        """
        return self._data

    @property
    def next_node(self):
        """
        This is a getter function for the node
        pointer
        """
        return self._next_node

    @data.setter
    def data(self, value):
        """
        This is a setter function for the data value, which
        performs exception handling

        Args:
            value(int): the parameter to be used for the
            self._data attribute
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @next_node.setter
    def next_node(self, value):
        """
        This is a setter function for the node pointer

        Args:
            value(NodeObject): the value for the pointer value
            used in place of self._next_node
        """
        if value is None or isinstance(value, Node):
            self._next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
This is another Python class
"""


class SinglyLinkedList:
    """
    This class contains functions that insert new nodes into the
    linked list such that the nodes are in ascending order
    """
    def __init__(self):
        """
        This is a custom constructor for the head node
        """
        self._head = None

    def __str__(self):
        """
        This function prints the resulting linked list

        Return:
            A list representig the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """
        This function performs the insertion operation such that
        the resulting list is an ordered linked list with elements
        in an ascending order

        Args:
            value(NodeObjcet): the pointer variable that the function
            will update during the operation
        """
        new_node = Node(value)
        if self._head is None or self._head.data >= value:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None:
                if current.next_node.data < value:
                    current = current.next_node
            if current.next_node is None or current.next_node.data > value:
                new_node.next_node = current.next_node
                current.next_node = new_node
            else:
                new_node.next_node = current.next_node
                current.next_node = new_node
