- Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

- You may return the answer in any order.

### Example 1:
```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

### Example 2:
```
Input: n = 1, k = 1
Output: [[1]]
```

### Solution: 
- backtracking
```python
class Solution(object):
    def combine(self, n, k):
        def backtracking(r, res, ne):
            if r == 0:
                ans.append(res[:])
            else:
                for i in range(ne, n+1):
                    res.append(i)
                    backtracking(r-1, res, i+1)
                    res.pop()
        ans = []
        backtracking(k, [], 1)
        return ans
```