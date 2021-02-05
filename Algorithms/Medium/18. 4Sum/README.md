- Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

- Notice that the solution set must not contain duplicate quadruplets.

### Example 1:
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Solution: 
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def fourSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return res
            # k = 2 return ans
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    # if return something, append it
                    # recursive utill k = 2
                    for _, set in enumerate(fourSum(nums[i+1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            l = 0
            r = len(nums) - 1
            while (l < r):
                sum = nums[l] + nums[r]
                # if smaller or the same number, l + 1
                if sum < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                # if bigger or the same number, r + 1 
                elif sum > target or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    r -= 1
                # if eqaul
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
                
        nums.sort()
        return fourSum(nums, target, 4)
```