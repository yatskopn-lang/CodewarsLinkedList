"""Swap Node Pairs In Linked List"""

#from preloaded import Node

class Node:
    """
    Represents a Node class.
    """
    def __init__(self, next=None):
        self.next = next

#my code
def swap_pairs(head):
    """
    Swaps adjacent pairs of nodes in the linked
    list and returns the new head while maintaining
    all internal connections.
    """
    prob = head
    if head and head.next:
        new_head = head.next
    else:
        new_head = head
    priv = None
    while prob and prob.next:
        node1 = prob
        node2 = prob.next
        node1.next= prob.next.next
        node2.next = node1
        if priv:
            priv.next = node2
        priv = node1
        prob = prob.next
    return new_head
