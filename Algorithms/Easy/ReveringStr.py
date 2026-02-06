from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return
        for i in range(len(s) // 2):
            _ = s[i]
            s[i] = s[-i-1]
            s[-i-1] = _

if __name__=="__main__":
    solution = Solution()
    test1 = ["h","e","l","l","o"]
    solution.reverseString(test1)
    print(test1)