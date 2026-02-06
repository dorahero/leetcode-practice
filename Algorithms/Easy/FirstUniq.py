class Solution:
    def firstUniqChar(self, s: str) -> int:
        cntMap = {x: 0 for x in s}
        for i in range(len(s)):
            cntMap[s[i]] += 1
        res = -1
        for i, ss in enumerate(s):
            if cntMap[ss] == 1:
                return i
        return res
        
if __name__=="__main__":
    solution = Solution()
    test1 = "loveleetcode"
    res = solution.firstUniqChar(test1)
    print(res)