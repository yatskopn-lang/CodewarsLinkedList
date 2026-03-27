"""Linked Lists - Append"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

#my code
def append(listA, listB):
    """
    Appends one linked list to another,
    returning the concatenated list.
    """
    if not listA and not listB:
        return None
    if not listA:
        return listB
    if not listB:
        return listA
    prob = listA
    while prob and prob.next:
        prob = prob.next
    prob.next = listB
    return listA
