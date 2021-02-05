- Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

- If target is not found in the array, return [-1, -1].

### Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Solution: 
```python
class Solution(object):
    def searchRange(self, nums, target):
        ans = [-1, -1]
        for i, n in enumerate(nums):
            if n == target:
                if ans[0] == -1:
                    ans[0] = i
                    ans[1] = i
                else:
                    ans[1] = i
        return ans
        
```