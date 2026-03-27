"""Linked Lists - Move Node"""

class Node(object):
    """
    Represents a Node class.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    Represents a Context class.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

#my code
def move_node(source, dest):
    """
    Moves the front node from the source
    list to the front of the destination list
    and returns both updated heads in a Context object.
    """
    first = source.data
    source = source.next
    new_dest = Node(first)
    new_dest.next = dest
    return Context(source, new_dest)
