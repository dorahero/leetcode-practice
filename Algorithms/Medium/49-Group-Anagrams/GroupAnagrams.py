from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        ans = []
        _ = defaultdict(list)
        for s in strs:
            tmp = "".join(sorted(s))
            _[tmp].append(s)
        for i in _:
            ans.append(_[i])
        return ans

if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res) 