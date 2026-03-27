"""Linked Lists - Length & Count"""

#from preloaded import Node

#Node is defined in preloaded:
class Node:
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node: Node) -> int:
    """
    Linked Lists - Length & Count
    """
    prob = node
    size = 0
    while prob:
        size += 1
        prob = prob.next
    return size

def count(node: Node, data) -> int:
    """
    Counts the occurrences of a specific
    data value in a linked list.
    """
    counting = 0
    prob = node
    while prob:
        if prob.data == data:
            counting += 1
        prob = prob.next
    return counting
