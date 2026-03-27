"""Linked Lists - Remove Duplicates"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

#my code
def remove_duplicates(head):
    """
    Iterates through a sorted linked
    list and removes any consecutive nodes with
    identical data values.
    """
    if not head:
        return head
    prob = head
    while prob and prob.next:
        if prob.data == prob.next.data:
            while prob.next and prob.data == prob.next.data:
                prob.next = prob.next.next
        prob = prob.next
    return head
