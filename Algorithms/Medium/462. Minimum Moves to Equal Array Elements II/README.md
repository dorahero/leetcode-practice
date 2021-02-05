- Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
### Example 1:
```
Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

### Solution: 
```python
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        # find the median
        goal = nums[len(nums)//2]
        # find sum of all number's distance with median
        return sum([abs(n-goal) for n in nums])
```