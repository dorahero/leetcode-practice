class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        tmp1 = ListNode(0)
        h_start = tmp1
        tmp2 = ListNode(0)
        h_end = tmp2
        while head:
            if head.val < x:
                tmp1.next = ListNode(head.val)
                tmp1 = tmp1.next
            else:
                tmp2.next = ListNode(head.val)
                tmp2 = tmp2.next
            head = head.next
        # contact 2 List
        tmp1.next = h_end.next
        if h_start.next:
            ans = h_start.next
        else:
            ans = ListNode("") 
        return ans

if __name__ == '__main__':
    h = [1,6,2,4,3,1,2,5,2]
    head = _ = ListNode(h[0])
    for i in h[1:]:
        _.next = ListNode(i)
        _ = _.next
    res = Solution().partition(head = head, x = 3)
    while res:
        print(res.val)
        res = res.next