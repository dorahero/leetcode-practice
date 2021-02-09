class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        _ = [0 for x in range(n)]
        # record 0 location
        tmp = set()
        for i in range(m):
            counter = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    tmp.add(j)
                    counter += 1
            if counter > 0:
                matrix[i] = _
        for t in tmp:
            for x in range(m):
                matrix[x][t] = 0
        return matrix

if __name__ == '__main__':
    res = Solution().setZeroes([[0,0,0,5],
                                [4,3,1,4],
                                [0,1,1,4],
                                [1,2,1,3],
                                [0,0,1,1]])
    print(res)  