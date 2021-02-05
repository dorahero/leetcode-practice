- Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
### Example 1:
```
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
```

### Example 2:
```
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```

### Solution: 
```python
class Solution:
    def find132pattern(self, nums):
        if len(nums) <=2:
            return False
        # lowerbound
        third = float('-inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            # first < second
            if nums[i] < third:
                return True
            else:
                # third < second
                while stack and stack[-1] < nums[i]:
                    third = stack.pop()
            stack.append(nums[i])
        return False
```