import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower()

        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True

if __name__=="__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    res = solution.isPalindrome(s)
    print(res)