"""Can you get the loop"""

def loop_size(node):
    """
    Detects a cycle in a linked list
    using Floyd's cycle-finding
    algorithm and calculates the number of
    nodes within that loop.
    """
    slow = node
    fast = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    size = 0
    fast = slow.next
    while fast != slow:
        fast = fast.next
        size += 1
    return size + 1
