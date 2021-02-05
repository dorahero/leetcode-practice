- Given a string s, find the length of the longest substring without repeating characters. 

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
### Example 2:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Solution: 
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        ans = 0
        for j in range(len(s)):
            _ = set()
            for i in s[j:]:
                if i not in _:
                    _.add(i)
                    ans = max(len(_), ans)
                else:
                    break
                
        return ans
```