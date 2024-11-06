#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# MY_PGP
# File description:
# Node
#

class Node:
    """
    Node class
    It represents a node in the tree
    It has a value and a list of children
    """

    def __init__(self, value : int) -> None:
        """
        Constructor of the Node class
        :param self: an instance of the Node class
        :param value: the value of the node
        """
        self.children = []
        self.value = value

    def add_child(self, child: 'Node' or int) -> 'Node':
        """
        Add a child to the node
        :param self: an instance of the Node class
        :param child: the child to add
        :return: the child added
        """
        if isinstance(child, int):
            self.children.append(Node(child))
        else:
            self.children.append(child)
        return self.children[-1]

    def add_children(self, children: list) -> list:
        """
        Add children to the node
        :param self: an instance of the Node class
        :param children: the children to add
        """
        self.children.extend(children)
        return children

    def remove_child(self, child : 'Node') -> None:
        """
        Remove a child from the node
        :param self: an instance of the Node class
        :param child: the child to remove
        """
        self.children.remove(child)

    def remove_children(self, children : list) -> None:
        """
        Remove children from the node
        :param self: an instance of the Node class
        :param children: the children to remove
        """
        for child in children:
            if child in self.children:
                self.children.remove(child)

    def clear_children(self) -> None:
        """
        Clear the children of the node
        :param self: an instance of the Node class
        """
        self.children.clear()

    def get_value(self) -> int:
        """
        Get the value of the node
        :param self: an instance of the Node class
        :return: the value of the node
        """
        return self.value

    def get_child(self, index : int) -> 'Node':
        """
        Get a child of the node
        :param self: an instance of the Node class
        :param index: the index of the child to get
        :return: the child at the index
        """
        return self.children[index]

    def get_children(self) -> list:
        """
        Get the children of the node
        :param self: an instance of the Node class
        :return: the children of the node
        """
        return self.children

    def set_value(self, value) -> None:
        """
        Set the value of the node
        :param self: an instance of the Node class
        :param value: the value to set
        """
        self.value = value

    def set_children(self, children) -> None:
        """
        Set the children of the node
        :param self: an instance of the Node class
        :param children: the children to set
        """
        self.children = children

    def is_leaf(self) -> bool:
        """
        Check if the node is a leaf
        :param self: an instance of the Node class
        :return: True if the node is a leaf, False otherwise
        """
        return len(self.children) == 0

    def get_max_depth(self) -> int:
        """
        Get the maximum depth of the tree
        :param self: an instance of the Node class
        :return: the maximum depth of the tree
        """
        if self.is_leaf():
            return 0
        return 1 + max([child.get_max_depth() for child in self.children])

    def get_min_depth(self) -> int:
        """
        Get the minimum depth of the tree
        :param self: an instance of the Node class
        :return: the minimum depth of the tree
        """
        if self.is_leaf():
            return 0
        return 1 + min([child.get_min_depth() for child in self.children])

    def get_min_value_at_depth(self, depth : int) -> int:
        """
        Get the minimum value at a certain depth
        :param self: an instance of the Node class
        :param depth: the depth to check
        :return: the minimum value at the depth. If the depth is greater than the maximum depth, return -1
        """
        if depth == 0:
            return self.value
        if self.get_max_depth() < depth:
            return -1
        min_value = -1
        for child in self.children:
            value = child.get_min_value_at_depth(depth - 1)
            if min_value == -1:
                min_value = value
            if min_value > value > 0:
                min_value = value
        return min_value

    def get_max_value_at_depth(self, depth: int) -> int:
        """
        Get the maximum value at a certain depth
        :param self: an instance of the Node class
        :param depth: the depth to check
        :return: the maximum value at the depth. If the depth is greater than the maximum depth of the tree, return -1
        """
        if depth == 0:
            return self.value
        if self.get_max_depth() < depth:
            return -1
        max_value = -1
        for child in self.children:
            value = child.get_max_value_at_depth(depth - 1)
            if value > max_value:
                max_value = value
        return max_value

    def get_value_roads(self) -> list:
        """
        Get the roads of the tree
        :param self: an instance of the Node class
        :return: the roads of the tree
        """
        if self.is_leaf():
            return [[self.value]]
        return [[self.value] + road for child in self.children for road in child.get_value_roads()]

    def display_tree(self, indentation : int = 0) -> None:
        """
        Display the tree
        :param self: an instance of the Node class
        :param indentation: the indentation of the node
        """
        if self.is_leaf():
            print(str(self.value))
            return
        print(str(self.value) + " ->")
        for child in self.children:
            print("|   " * (indentation + 1), end="")
            child.display_tree(indentation + 1)

    def __str__(self) -> str:
        """
        Print the node
        :param self: an instance of the Node class
        :return: the string to print
        """
        self.display_tree()
        return ""

    def __repr__(self) -> str:
        """
        Print the node
        :param self: an instance of the Node class
        :return: the string to print
        """
        return self.__str__()

    def __eq__(self, other : 'Node') -> bool:
        """
        Compare two nodes
        :param self: an instance of the Node class
        :param other: the other node to compare
        :return: True if the nodes are equal, False otherwise
        """
        return self.value == other.value and self.children == other.children

    def __ne__(self, other : 'Node') -> bool:
        """
        Compare two nodes
        :param self: an instance of the Node class
        :param other: the other node to compare
        :return: True if the nodes are different, False otherwise
        """
        return not self.__eq__(other)

    def __lt__(self, other : 'Node') -> bool:
        """
        Compare two nodes
        :param self: an instance of the Node class
        :param other: the other node to compare
        :return: True if the first node is less than the second, False otherwise
        """
        return self.value < other.value

    def __gt__(self, other : 'Node') -> bool:
        """
        Compare two nodes
        :param self: an instance of the Node class
        :param other: the other node to compare
        :return: True if the first node is greater than the second, False otherwise
        """
        return self.value > other.value
