### Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

### Example 1:
```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:
```
Input: l1 = [], l2 = []
Output: []
```

### Example 3:
```
Input: l1 = [], l2 = [0]
Output: [0]
```

### Constraints:
- The number of nodes in both lists is in the range [0, 50].  
- -100 <= Node.val <= 100  
- Both l1 and l2 are sorted in non-decreasing order.  

### Solution: 
```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l = []
        s = []
        for t in [l1, l2]:
            i = 0
            while 1:
                if t != None:
                    i += 1
                    t = t.next
                else:
                    break
            s.append(i)
        while 1:
            if s[0] > 0 and s[1] > 0:
                if l1.val < l2.val:
                    l.append(l1.val)
                    l1 = l1.next
                    s[0] -= 1
                elif l1.val > l2.val:
                    l.append(l2.val)
                    l2 = l2.next
                    s[1] -= 1
                else:
                    l.append(l1.val)
                    l1 = l1.next
                    s[0] -= 1
                    l.append(l2.val)
                    l2 = l2.next
                    s[1] -= 1
            elif s[0] > 0 and s[1] == 0:
                l1_l = s[0]
                for i in range(l1_l):
                    l.append(l1.val)
                    l1 = l1.next
                    s[0] -= 1
            elif s[0] == 0 and s[1] > 0:
                l2_l = s[1]
                for i in range(l2_l):
                    l.append(l2.val)
                    l2 = l2.next
                    s[1] -= 1
            else:
                break
        # create a ListNode with head = 0
        head = cur = ListNode(0)
        for l_v in l:
            # set head with change cur
            cur.next = ListNode(l_v)
            cur = cur.next
        return head.next
```