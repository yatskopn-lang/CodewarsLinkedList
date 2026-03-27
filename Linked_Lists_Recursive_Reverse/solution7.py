"""Linked Lists - Recursive Reverse"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

#my code
def reverse(head):
    """
    Reverses the linked list in place by reassigning
    the next pointers of each node and returns the new head.
    """
    if not head:
        return None
    priv = None
    prob = head
    while prob:
        next_el = prob.next
        priv_el = prob
        prob.next = priv
        priv = priv_el
        prob = next_el
    return priv
