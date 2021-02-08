# class Solution(object):
#     def rotate(self, matrix):
#         n = len(matrix)
#         m = len(matrix[0])
#         ans = [[0 for i in range(m)] for j in range(n)]
#         # 0, 0 to 0, m
#         # 0, 1 to 1, m ...
#         for i, x in enumerate(matrix):
#             for j, y in enumerate(x):
#                 ans[j][m-i-1] = matrix[i][j]
#         return ans
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # how many square
        c = n // 2
        # square : outside to inside
        for i in range(c):
            # left bottom right side for square
            for x in range(3):
                # replace : left side switch with top side 
                # and bottom, and so on
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
        return matrix
if __name__ == "__main__":
    res = Solution().rotate([[ 2,29,20,26,16,28]
                            ,[12,27, 9,25,13,21]
                            ,[32,33,32, 2,28,14]
                            ,[13,14,32,27,22,26]
                            ,[33, 1,20, 7,21, 7]
                            ,[ 4,24, 1, 6,32,34]])
                            
                            # [[ 4,33,13,32,12, 2]
                            # ,[24, 1,14,33,27,29]
                            # ,[ 1,20,32,32, 9,20]
                            # ,[ 6, 7,27, 2,25,26]
                            # ,[32,21,22,28,13,16]
                            # ,[34, 7,26,14,21,28]]

                            # [[ 4,33,13,32,12, 2]
                            # ,[24, 1,14,25,27,29]
                            # ,[ 1,33,32, 2, 9,20]
                            # ,[ 6, 7,32,27,22,26]
                            # ,[32,21,20,28,13,16]
                            # ,[34, 7,26,14,21,28]]    
    print(res)