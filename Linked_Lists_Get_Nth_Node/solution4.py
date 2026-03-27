"""Linked Lists - Get Nth Node"""

#from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#my code
def get_nth(node, index):
    """
    Retrieves the node at the specified index
    from the linked list or raises a ValueError
    if the index is invalid.
    """
    if node is None:
        raise ValueError('Your node is None')
    i = 0
    while node:
        if i == index:
            return node
        i += 1
        node = node.next
    raise ValueError('Index is out of the range')
