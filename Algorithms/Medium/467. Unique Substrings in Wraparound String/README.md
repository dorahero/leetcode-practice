- Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".  

- Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.  

- Note: p consists of only lowercase English letters and the size of p might be over 10000.  

### Example 1:
```
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
```
### Example 2:
```
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
```

### Solution: 
```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        left = 0
        # init every start word counter
        cnt = [0] * 26
        
        for right in range(len(p)):
            if right>=1 and ord(p[right]) - ord(p[right-1]) == 1 or p[right] == 'a' and p[right-1] == 'z':
                # if is coutinulity word
                cnt[ord(p[right]) - ord('a')] = max(right-left+1, cnt[ord(p[right]) - ord('a')])
                
            else:
                left = right
                cnt[ord(p[right]) - ord('a')] = max(1, cnt[ord(p[right]) - ord('a')])
                
        return sum(cnt)
```