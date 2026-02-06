from linked_list_utils import ListNode, print_linked_list, create_linked_list
class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast = head, head

        # half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse
        node = None
        while slow:
            tmp = slow.next
            slow.next = node
            node = slow
            slow = tmp
        
        first, second = head, node
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True

def main():
    head = create_linked_list([1,2,1,3,4])

    print_linked_list(head)
    
    solution = Solution()
    print(solution.isPalindrome(head))
        
    head2 = create_linked_list([1, 2])
    
    print_linked_list(head2)

    print(solution.isPalindrome(head2))


if __name__ == "__main__":
    main()
