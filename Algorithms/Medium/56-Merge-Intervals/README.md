- Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
### Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

### Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Solution: 
```python
class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        ans = []
        x, y = intervals[0]
        for i, j in enumerate(intervals[1:]):
            print(x,y)
            if y < j[0]:
                if [x, y] not in ans:
                    ans.append([x,y])
                if i == len(intervals)-2:
                    ans.append(j)
                x, y = j
            else:
                y = max(y,j[1])
                x = min(x, j[0])
                if i == len(intervals)-2:
                    ans.append([x,y])

        return ans
```