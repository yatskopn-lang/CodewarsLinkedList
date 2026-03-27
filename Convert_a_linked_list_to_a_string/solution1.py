"""Convert a linked list to a string"""

class Node():
    """
    Represents a Node class.
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#my code
def stringify(node):
    """
    This function converts a linked list to a string.
    """
    if node is None:
        return 'None'
    res = []
    res.append(str(node.data))
    while node.next != None:
        res.append(str(node.next.data))
        node = node.next
    res.append('None')
    res = ' -> '.join(res)
    return res
