- Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

### Example 1:
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

### Example 2:
```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

### Solution: 
```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        h = ListNode(0)
        h_tmp = h
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
```

### Result
![](./result.PNG )