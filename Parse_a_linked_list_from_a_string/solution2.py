"""Parse a linked list from a string"""

class Node:
    """
    Represents a Node class.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#from preloaded import Node

#my code
def linked_list_from_string(list_repr: str) -> Node | None:
    """
    This function parses a linked list from a string.
    """
    list_repr = list_repr.split(' -> ')
    list_repr = list_repr[::-1]
    for i, el in enumerate(list_repr):
        if i == 0:
            res = None
        else:
            res = Node(int(el), res)
    return res
