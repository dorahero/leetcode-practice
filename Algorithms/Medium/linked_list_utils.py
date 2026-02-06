# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


def print_linked_list(head):
    """Helper function to print linked list"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))


def create_linked_list(values, pos=None):
    """Helper function to create a linked list from a list of values
    
    Args:
        values: list of values to create the linked list
        pos: optional parameter, if provided, the last node's next will point to the node at this index (creating a cycle)
    
    Returns:
        head of the linked list
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # If pos is provided, create a cycle by pointing the last node to the node at index pos
    if pos is not None and 0 <= pos < len(nodes):
        current.next = nodes[pos]
    
    return head
