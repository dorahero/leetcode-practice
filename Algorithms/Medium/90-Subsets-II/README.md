- Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

- The solution set must not contain duplicate subsets. Return the solution in any order.

### Example 1:
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

### Solution: 
```python
class Solution(object):
    def subsetsWithDup(self, nums):
        def backtracking(r, res, ne):
            if r == 0 and res[:] not in ans:
                ans.append(res[:])
            else:
                for i in range(ne, n):
                    res.append(nums[i])
                    backtracking(r-1, res, i+1)
                    res.pop()
        ans = [[]]
        n = len(nums)
        nums = sorted(nums)
        for k in range(1, n+1):
            backtracking(k, [], 0)
        return ans
```