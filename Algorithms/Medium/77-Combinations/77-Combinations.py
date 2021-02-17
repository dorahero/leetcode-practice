class Solution(object):
    def combine(self, n, k):
        def backtracking(r, res, ne):
            if r == 0:
                ans.append(res[:])
            else:
                for i in range(ne, n+1):
                    res.append(i)
                    backtracking(r-1, res, i+1)
                    res.pop()
        ans = []
        backtracking(k, [], 1)
        return ans

if __name__ == '__main__':
    res = Solution().combine(n = 20, k = 16)
    print(res)  