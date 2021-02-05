- Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.  

- Notice that the solution set must not contain duplicate triplets.  

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

```

### Solution: 
```python
class Solution(object):
    def threeSum(self, nums):
        def two_sum(arr, target):
            l, r, other_two = 0, len(arr)-1, set()
            while l < r:
                if arr[l] + arr[r] > target:
                    r -= 1
                elif arr[l] + arr[r] < target:
                    l += 1
                else: 
                    tmp = (arr[l], arr[r])
                    l, r = l+1, r-1
                    # set can avoid duplication
                    other_two.add(tmp)
            return other_two
            
        nums = sorted(nums)
        ans = []
        if len(nums) < 3 or nums[0] > 0:
            return ans
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                # distinct nums[i]
                diff = 0 - nums[i]
                # if nums[i+1:] have sum of two number = diff, return
                two_sum_ok = two_sum(nums[i+1:], diff)
                # contact result
                for t in two_sum_ok:
                    _ = [nums[i], t[0], t[1]]
                    ans.append(_)
        return ans
```