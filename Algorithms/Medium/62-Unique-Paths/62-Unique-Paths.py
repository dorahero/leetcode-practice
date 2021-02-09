class Solution(object):
    def uniquePaths(self, m, n):
        def factorial(num):
            res = 1
            for i in range(1, num+1):
                res *= i
            return res
        def numPermutation(x, y):
            return factorial(x+y)/(factorial(x)*factorial(y))
        # permutation of down and right
        ans = numPermutation(m-1, n-1)
        return ans

if __name__ == '__main__':
    res = Solution().uniquePaths(3, 7)
    print(res)  