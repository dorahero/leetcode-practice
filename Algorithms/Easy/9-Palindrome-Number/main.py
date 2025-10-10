class Solution(object):
    def isPalindrome(self, x):
            if x >= 0:
                a = []
                for i in range(len(str(x))):
                    a.append(x // (10**i) % 10)
                sum = 0
                for i, j in enumerate(a):
                    sum += j*(10**(len(str(x))-1-i))
                if sum == x:
                    return True
                else:
                    return False
            else:
                return False

solution = Solution()
result = solution.isPalindrome(123)
print(result)  

