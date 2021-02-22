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
    h = [1,2,3,4,5]
    head = _ = ListNode(h[0])
    for i in h[1:]:
        _.next = ListNode(i)
        _ = _.next
    res = Solution().removeNthFromEnd(head, 2)
    while res:
        print(res.val)
        res = res.next