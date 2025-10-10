import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        # only use min(str) to compare max(str)
        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1     

solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)  

