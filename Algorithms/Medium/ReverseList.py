import env
from Algorithms.function.LinkNodeComponent import ListNode, print_linked_list, create_linked_list
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev


def main():
    head = create_linked_list([4, 5, 1, 9, 3, 5])
    
    print("Original linked list:")
    print_linked_list(head)
    
    solution = Solution()
    prev = solution.reverseList(head)
    
    print_linked_list(prev)

if __name__ == "__main__":
    main()
