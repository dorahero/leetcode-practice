- Given an m x n board and a word, find if the word exists in the grid.

- The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example 1:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Solution 1: 
```python
class Solution(object):
    def exist(self, board, word):
        def find(i, j, x, di):
            direction = [(0, 1), (1,0), (0, -1), (-1, 0)]
            if ans[0]:
                return True
            for k, d in enumerate(direction):
                if k == di:
                    continue
                if 0 <= x < len(word)-1 and 0 <= i+d[0] < n and 0 <= j+d[1] < m and board[i+d[0]][j+d[1]] == word[x+1] and (i+d[0], j+d[1]) not in _:
                    if x+1 == len(word)-1:
                        ans.pop()
                        ans.append(True)
                        break
                    else:
                        _.append((i+d[0], j+d[1]))
                        find(i+d[0], j+d[1], x+1, (k+2) % 4)
            _.pop(-1)
            
        ans = [False]
        m = len(board[0])
        n = len(board)
        for i in range(n):
            for j in range(m):
                _ = []
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    _.append((i,j))
                    find(i, j, 0, 4)
                    if ans[0]:
                        break
        return ans[0]
```
### Solution 2: 
- DFS
```python
class Solution(object):
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j): return True
        return False
                
    def dfs(self, board, word, i, j):
        # if index out of range
        if i <= -1 or i >= len(board) or j <= -1 or j >= len(board[0]): return False
        # if passed before of not the word
        if board[i][j] == -1 or board[i][j] != word[0]: return False
        # if is the last word
        if len(word) == 1: return True
        
        temp, board[i][j] = board[i][j], -1
        # 4 direction
        if self.dfs(board, word[1:], i-1, j): return True
        if self.dfs(board, word[1:], i+1, j): return True
        if self.dfs(board, word[1:], i, j-1): return True
        if self.dfs(board, word[1:], i, j+1): return True
        # all False, let board[i][j] be the original value
        board[i][j] = temp
        return False
```