- Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.  

- The distance between two adjacent cells is 1.  
### Example 1:
```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

### Example 2:
```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

### Constraints:
- 1 <= nums.length <= 104  
- -104 <= nums[i] <= 104  
- nums contains distinct values sorted in ascending order.  
- -104 <= target <= 104  

### Solution: 
```python
class Solution(object):
    def updateMatrix(self, matrix):
        if matrix == None or len(matrix) == 0:
            return matrix
        w = len(matrix[0])
        h = len(matrix)
        s = []
        for i in range(h):
            for j in range(w):
                if matrix[i][j] != 0:
                    s.append([i, j, 0])
                    while s:
                        a, b, dist = s.pop(0)
                        # if next element is 0, set the dist
                        if matrix[a][b] == 0:
                            matrix[i][j] = dist
                            s = []
                            break
                        # move to up, down, right, left
                        for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                            xa = x+a
                            yb = y+b
                            # next element in correct area
                            if 0<=xa<h and 0<=yb<w:
                                s.append([xa, yb, dist+1])
        return matrix
```