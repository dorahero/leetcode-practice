class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)       
        res = 0
        nn = len(str(n))
        for i in range(nn):
            res += ((n // (10 ** (nn-1-i))) % 10) * (10 ** i)
            if res > 2**31 - 1:
                return 0
        if n != x:
            res = -res
        return res

if __name__=="__main__":
    solution = Solution()
    test1 = -321
    res = solution.reverse(test1)
    print(res)