from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(s) for s in strs])
        ans = ""
        for i in range(n):
            target = strs[0][i]
            for s in strs:
                if target != s[i]:
                    return ans
            ans += s[i]
        return ans

if __name__=="__main__":
    solution = Solution()
    strs = [""]
    res = solution.longestCommonPrefix(strs)
    print(res)