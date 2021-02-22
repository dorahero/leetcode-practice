# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        pos = 1

        curr = head
        prev = None

        while pos < left:
            prev = curr
            curr = curr.next

            pos += 1
        lastOne = prev
        # the first one to be reverse => Last one reversed
        firstReverse = curr

        while pos <= right:
            nxt = curr.next
            # next to be prev one ListNode
            curr.next = prev
            # move to next
            prev = curr
            curr = nxt

            pos += 1
        # if right != left
        if lastOne:
            # => First one reversed
            lastOne.next = prev
        else:
            head = prev
        # Last one reversed => first one remained
        firstReverse.next = curr


        return head
        

if __name__ == '__main__':
    h = [3,5,7]
    head = _ = ListNode(h[0])
    for i in h[1:]:
        _.next = ListNode(i)
        _ = _.next
    res = Solution().reverseBetween(head = head, left = 2, right = 3)
    while res:
        print(res.val)
        res = res.next