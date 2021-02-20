- Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

- You should preserve the original relative order of the nodes in each of the two partitions.

### Example 1:
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

### Example 2:
```
Input: head = [2,1], x = 2
Output: [1,2]
```

### Solution: 
```python
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
```