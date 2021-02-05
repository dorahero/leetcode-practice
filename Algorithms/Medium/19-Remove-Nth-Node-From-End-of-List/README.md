- Given the head of a linked list, remove the nth node from the end of the list and return its head.

- Follow up: Could you do this in one pass?

### Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Solution: 
```python
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
```