class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # add a ListNode(0) at the frount of head 
        dum = ListNode(0, head)
        left = dum
        right = head
        while n > 0:
            right = right.next
            n -= 1
        # right is for count 
        while right:
            left = left.next
            right = right.next
        # skip target one
        left.next = left.next.next
            
        return dum.next
if __name__ == "__main__":
    l1 = ListNode(1)
    for i in range(9):
        l1.next = ListNode(2)
    res = Solution().removeNthFromEnd(l1, 2)