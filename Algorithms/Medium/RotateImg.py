from typing import List

class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        c = n // 2
        for i in range(c):
            for x in range(3):
                for y in range(n-2*i-1):
                    if x == 0:
                        _ = matrix[y+i][-1-i]
                        matrix[y+i][-1-i] = matrix[0+i][y+i]
                        matrix[0+i][y+i] = _
                    elif x == 1:
                        _ = matrix[-1-i][-1-y-i]
                        matrix[-1-i][-1-y-i] = matrix[0+i][y+i]
                        matrix[0+i][y+i] = _
                    elif x == 2:
                        _ = matrix[-1-y-i][0+i]
                        matrix[-1-y-i][0+i] = matrix[0+i][y+i]
                        matrix[0+i][y+i] = _


if __name__=="__main__":
    solution = Solution()
    test1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(test1)
    print(test1)