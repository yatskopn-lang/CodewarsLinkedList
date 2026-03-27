"""Linked Lists - Alternating Split"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    Represents a Context class.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Splits a linked list into two separate lists
    by alternating nodes from the original list
    and returns them within a Context object.
    """
    if not head.next:
        raise ValueError('Need more nodes')
    prob1 = head
    prob2 = head.next
    def find_first(prob1):
        if prob1 is None:
            return None
        first = None
        try:
            new_next =  prob1.next.next
        except AttributeError:
            new_next = None
        first = Node(prob1.data)
        first.next = find_first(new_next)
        return first
    def find_second(prob2):
        if prob2 is None:
            return None
        second = None
        try:
            new_next = prob2.next.next
        except AttributeError:
            new_next = None
        second = Node(prob2.data)
        second.next = find_second(new_next)
        return second
    return Context(find_first(prob1), find_second(prob2))
