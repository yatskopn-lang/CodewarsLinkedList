"""Linked Lists - Sorted Insert"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

#my code
def sorted_insert(head, data):
    """
    Inserts a new node with the given data
    into its correct sorted position within
    a sorted linked list.
    """
    if not head:
        return Node(data)
    if data < head.data:
        new_head = Node(data)
        new_head.next = head
        return new_head
    prob = head
    while prob and prob.next:
        if data > prob.next.data:
            next_el = prob.next
            prob.next = Node(data)
            prob.next.next = next_el
            return head
        prob = prob.next
    prob.next = Node(data)
    return head
