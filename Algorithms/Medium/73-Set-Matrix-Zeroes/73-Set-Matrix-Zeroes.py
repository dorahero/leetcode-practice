class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        _ = [0 for x in range(n)]
        # record 0 location
        tmp = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    tmp.append((i, j))
        # replace not 0 to 0 on the cross
        for t in tmp:
            for x in range(m):
                matrix[x][t[1]] = 0
            matrix[t[0]] = _
        return matrix

if __name__ == '__main__':
    res = Solution().setZeroes([[0,0,0,5],
                                [4,3,1,4],
                                [0,1,1,4],
                                [1,2,1,3],
                                [0,0,1,1]])
    print(res)  