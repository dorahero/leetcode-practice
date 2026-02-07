class Solution:
    def climbStairs(self, n: int) -> int:
        def nCr(n, k):
            if k > n // 2:
                k = n - k
                
            result = 1
            for i in range(k):
                result = result * (n - i) // (i + 1)
                
            return result

        cnt = 0
        j = 0
        for i in range((n + 1) // 2, n+1):
            cnt += nCr(i, (n) // 2 + j)
            j -= 1
        
        return cnt


def main():
    n = 10
    solution = Solution()
    
    print(solution.climbStairs(n))

if __name__ == '__main__':
    main()