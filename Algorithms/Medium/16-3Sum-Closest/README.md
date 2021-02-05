- Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

### Example 1:
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

### Solution: 
```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        n = len(nums)
        # init diff
        closest_diff = float('Inf')
        res = []
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                tmp = [nums[i], nums[l], nums[r]]
                sum_tmp = sum(tmp)
                _ = sum_tmp - target
                # if closer
                if abs(_) < closest_diff:
                    res = tmp
                    closest_diff = abs(_)
                # if the smae
                if _ == 0:
                    return sum(res)
                elif _ < 0:
                    l += 1
                elif _ > 0:
                    r -= 1
        return sum(res)
```