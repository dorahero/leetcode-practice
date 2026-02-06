from linked_list_utils import ListNode, print_linked_list, create_linked_list
class Solution:
    def mergeTwoLists(self, list1, list2):
        dum = ListNode()
        cur = dum

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dum.next

def main():
    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1,3,4])
    
    solution = Solution()
    prev = solution.mergeTwoLists(list1, list2)
    
    print_linked_list(prev)

if __name__ == "__main__":
    main()
