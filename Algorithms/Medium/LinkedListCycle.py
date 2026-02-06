from linked_list_utils import ListNode, print_linked_list, create_linked_list

class Solution:
    def hasCycle(self, head) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False

def main():
    head = create_linked_list([3,2,0,-4], pos=2)
    
    solution = Solution()
    print(solution.hasCycle(head))


if __name__ == "__main__":
    main()
