class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(32):
            if (n >> i) & 1: # check the last one
                res += 1

        return res

solution = Solution()
print(solution.hammingWeight(2147483645))