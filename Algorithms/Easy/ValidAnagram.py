class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cntMaps = {x: 0 for x in s}
        for i in range(len(s)):
            cntMaps[s[i]] += 1
        cntMapt = {x: 0 for x in t}
        for i in range(len(t)):
            cntMapt[t[i]] += 1
        for k in set(s+t):
            if k not in cntMaps or k not in cntMapt:
                return False
            if cntMaps[k] != cntMapt[k]:
                return False
        
        return True

if __name__=="__main__":
    solution = Solution()
    s = "anagams"
    t = "nagaram"
    res = solution.isAnagram(s, t)
    print(res)