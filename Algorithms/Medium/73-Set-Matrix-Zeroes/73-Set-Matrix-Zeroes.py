from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols_num = len(matrix[0])
        row_ums = len(matrix)

        isFirstColZero = False
        isFirstRowZero = False
        # mark 1st col
        for i in range(cols_num):
            if matrix[0][i] == 0:
                isFirstColZero = True
                break
        for i in range(row_ums):
            if matrix[i][0] == 0:
                isFirstRowZero = True
                break
        
        # note with 1th col row
        for i in range(1, row_ums):
            for j in range(1, cols_num):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, cols_num):
            if matrix[0][i] == 0:
                for j in range(1, row_ums):
                    matrix[j][i] = 0
        
        for i in range(1, row_ums):
            if matrix[i][0] == 0:
                for j in range(1, cols_num):
                    matrix[i][j] = 0

        if isFirstColZero:
            for i in range(cols_num):
                matrix[0][i] = 0
        if isFirstRowZero:
            for i in range(row_ums):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[0,0,0,5],
                                [4,3,1,4],
                                [0,1,1,4],
                                [1,2,1,3],
                                [0,0,1,1]]
    Solution().setZeroes(matrix)
    print(matrix)  