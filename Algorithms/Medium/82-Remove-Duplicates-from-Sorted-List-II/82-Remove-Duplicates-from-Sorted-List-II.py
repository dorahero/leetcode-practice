# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        h = ListNode(0)
        h_tmp = h
        # record not distinct number
        tmp = set()
        start = head
        while head:
            _ = head.next
            if _:
                if _.val == head.val:
                    tmp.add(_.val)
            head = head.next
        while start:
            if start.val not in tmp:
                h_tmp.next = ListNode(start.val)
                h_tmp = h_tmp.next
            start = start.next
        if h.next:
            ans = h.next
        else:
            ans = ListNode("")
        return ans

if __name__ == '__main__':
    head = [1,2,3,3,4,4,5]
    inp = _ = ListNode(head[0])
    for h in head[1:]:
        _.next = ListNode(h)
        _ = _.next
    res = Solution().deleteDuplicates(head = inp)
    while res:
        print(res.val)
        res = res.next