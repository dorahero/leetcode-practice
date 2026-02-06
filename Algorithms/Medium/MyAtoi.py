import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        i = 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        
        num = 0
        while i < len(s) and s[i].isdigit():
            num = int(s[i]) + 10 * num
            print(num)
            i += 1
        
        num *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num


if __name__=="__main__":
    solution = Solution()
    s = "42"
    res = solution.myAtoi(s)
    print(res)