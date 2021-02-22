- Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

### Example 1:
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

### Example 2:
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

### Solution: 
```python
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
```
