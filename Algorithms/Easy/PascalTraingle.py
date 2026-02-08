from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res
        
        prev = res[1]
        for i in range(2, numRows):
            cur = [1] + [prev[j] + prev[j+1] for j in range(i-1)] + [1]
            res.append(cur)
            prev = cur
        return res

solution = Solution()
numRows = 5
print(solution.generate(numRows))