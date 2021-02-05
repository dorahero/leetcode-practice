class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def length(ln):
            c = 0
            while ln:
                c += 1
                ln = ln.next
            return c
        l1_len = length(l1)
        l2_len = length(l2)
        sum_l1 = 0
        # reverse and count the sum
        for i in range(l1_len):
            sum_l1 += l1.val*(10**i)
            l1 = l1.next
        sum_l2 = 0
        for j in range(l2_len):
            sum_l2 += l2.val*(10**j)
            l2 = l2.next
        s = str(sum_l1+sum_l2)
        # reverse again
        for x in range(1, 1+len(s)):
            if x == 1:
                l3 = cur = ListNode(int(s[-x]))
            else:
                cur.next =  ListNode(int(s[-x]))
                cur = cur.next
        return l3
    
        
if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    res = Solution().addTwoNumbers(l1, l2)