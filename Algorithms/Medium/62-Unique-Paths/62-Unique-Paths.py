class Solution(object):
    def uniquePaths(self, m, n):
        def factorial(num):
            res = 1
            for i in range(1, num+1):
                res *= i
            return res
        perimeter = (m-1)+(n-1)
        # permutation of down and right
        ans = factorial(perimeter)/(factorial(m-1)*factorial(n-1))
        return ans

if __name__ == '__main__':
    res = Solution().uniquePaths(3, 7)
    print(res)  