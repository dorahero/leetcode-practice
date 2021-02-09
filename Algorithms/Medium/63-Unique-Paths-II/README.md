- A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

- The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

- Now consider if some obstacles are added to the grids. How many unique paths would there be?

- An obstacle and space is marked as 1 and 0 respectively in the grid.

### Example 1:
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

### Example 2:
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

### Solution: 
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        ans = 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        # possible number matrix
        ans = [[0 for i in range(n)]for j in range(m)]
        ans[0][0] = 1
        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] == 0:
                    # the possible number of x,y is the sum of x-1,y and x, y-1
                    ans[x][y] += ans[x-1][y] if x-1 >= 0 else 0
                    ans[x][y] += ans[x][y-1] if y-1 >= 0 else 0
        return ans[-1][-1]
```