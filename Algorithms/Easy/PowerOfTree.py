class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3:
            if n == 1:
                return True
            return False
        tmp = n
        while tmp % 3 == 0 :
            tmp = tmp / 3
        if tmp != 1.0:
            return False
        return True

solution = Solution()

print(solution.isPowerOfThree(27))