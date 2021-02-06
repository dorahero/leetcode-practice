- Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Solution: 
```python
class Solution(object):
    def permute(self, nums):
        def nextNum(n):
            array = n[:]
            i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
            j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
            array[j], array[i - 1] = array[i - 1], array[j]
            array[i:] = reversed(array[i:])
            return array
        counter = 1
        for i in range(1, len(nums)+1):
            counter *= i
        ans = []
        nums = sorted(nums)
        ans.append(nums)
        for j in range(counter-1):
            nums  = nextNum(nums)
            ans.append(nums)

        return ans
```

### Result
![](./result.PNG )