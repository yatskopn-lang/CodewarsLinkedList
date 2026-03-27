"""Linked Lists - Insert Nth Node"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

#my code
def insert_nth(head, index, data):
    """
    Inserts a new node at a specific index
    in a linked list.
    """
    if not head:
        return Node(data)
    if index < 0:
        raise ValueError('Index out of range')
    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    i = 0
    prob = head
    while prob:
        if i + 1 == index:
            new_node = Node(data)
            new_node.next = prob.next
            prob.next = new_node
            return head
        i += 1
        prob = prob.next
    raise ValueError('Index out of range')
