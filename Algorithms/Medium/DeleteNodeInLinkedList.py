import env
from Algorithms.function.LinkNodeComponent import ListNode, print_linked_list, create_linked_list


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def main():
    # Create a linked list: 4 -> 5 -> 1 -> 9
    head = create_linked_list([4, 5, 1, 9])
    
    print("Original linked list:")
    print_linked_list(head)
    
    # Delete node with value 5 (the second node)
    solution = Solution()
    node_to_delete = head.next
    solution.deleteNode(node_to_delete)
    
    print("\nLinked list after deleting node with value 5:")
    print_linked_list(head)
    
    # Create another linked list: 1 -> 2 -> 3
    head2 = create_linked_list([1, 2, 3])
    
    print("\nAnother linked list:")
    print_linked_list(head2)
    
    # Delete node with value 2 (the second node)
    node_to_delete2 = head2.next
    solution.deleteNode(node_to_delete2)
    
    print("After deleting node with value 2:")
    print_linked_list(head2)


if __name__ == "__main__":
    main()
