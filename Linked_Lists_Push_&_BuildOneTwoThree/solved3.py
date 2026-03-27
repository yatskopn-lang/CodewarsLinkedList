"""Linked Lists - Push & BuildOneTwoThree"""

#from preloaded import Node

class Node:
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

#my code
def push(head, data):
    """
    Adds a new node with the specified data
    to the beginning of the linked list.
    """
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    """
    Constructs a linked list containing
    values 1, 2, and 3 by pushing them in reverse order.
    """
    res = None
    i = 3
    while i >= 1:
        res = push(res, i)
        i -= 1
    return res
