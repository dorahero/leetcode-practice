class Solution(object):
    def spiralOrder(self, matrix):
        def direction(n):
            step = [(0, 1), (1,0), (0, -1), (-1, 0)]
            return step[n % 4]
        n = len(matrix)
        m = len(matrix[0])
        en = n*m
        ans = []
        i = 0
        j = 0
        counter = []
        c = 0
        while len(ans) < en: 
            if (i, j) not in counter and 0<=i<n and 0<=j<m:
                tmp = matrix[i][j]
                counter.append((i, j))
                ans.append(tmp)
                d = direction(c)
                i += d[0]
                j += d[1]
            # change direction
            else:
                d = direction(c)
                i -= d[0]
                j -= d[1]
                c += 1
                d = direction(c)
                i += d[0]
                j += d[1]

        return ans
if __name__ == '__main__':
    res = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(res)  