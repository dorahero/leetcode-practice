### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:
- 2 <= nums.length <= 103  
- -109 <= nums[i] <= 109  
- -109 <= target <= 109  

### Solution: 
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if target == nums[i] + nums[j+i+1]:
                    return [i, j+i+1]
        return None
        
```