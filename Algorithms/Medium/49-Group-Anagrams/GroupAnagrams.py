class Solution(object):
    def groupAnagrams(self, strs):
        ans = []
        _ = {}
        for s in strs:
            tmp = "".join(sorted(list(s)))
            if tmp not in _:
                _[tmp] = [s]
            else:
                _[tmp].append(s)
        for i in _:
            ans.append(_[i])
        return ans


if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)  