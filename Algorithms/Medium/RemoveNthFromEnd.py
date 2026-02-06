from linked_list_utils import ListNode, print_linked_list, create_linked_list
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        # go first
        for _ in range(n): 
            fast = fast.next
        if not fast: 
            return head.next
        while fast.next: 
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

def main():
    head = create_linked_list([4, 5, 1, 9, 3, 5])
    
    print("Original linked list:")
    print_linked_list(head)
    
    solution = Solution()
    solution.removeNthFromEnd(head, 2)
    
    print_linked_list(head)

if __name__ == "__main__":
    main()
