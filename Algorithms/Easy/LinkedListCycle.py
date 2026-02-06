import env

from Algorithms.function.LinkNodeComponent import ListNode, print_linked_list, create_linked_list
class Solution:
    def hasCycle(self, head) -> bool:
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # if cycle must in 
            if fast == slow:
                return True
    
        return False

def main():
    head = create_linked_list([3,2,0,-4], pos=2)
    
    solution = Solution()
    print(solution.hasCycle(head))


if __name__ == "__main__":
    main()
