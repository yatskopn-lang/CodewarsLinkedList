"""Linked Lists - Front Back Split"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

#my code
def front_back_split(source, front, back):
    """
    Splits a linked list into two halves (front and back).
    If the list has an odd number of nodes, the extra
    node is placed in the front half.
    """
    if not source or not source.next:
        raise ValueError('Need more nodes')
    fast = source.next
    slow = source
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    middle_node = slow.next
    slow.next = None
    front.data = source.data
    front.next = source.next
    back.data = middle_node.data
    back.next = middle_node.next
