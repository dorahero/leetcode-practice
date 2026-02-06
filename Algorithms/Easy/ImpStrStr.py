class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not hasattr or not needle or len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1

if __name__=="__main__":
    solution = Solution()
    haystack = "mississippi"
    needle = "issip"
    res = solution.strStr(haystack, needle)
    print(res)