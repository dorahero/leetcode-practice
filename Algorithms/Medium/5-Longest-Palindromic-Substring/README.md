- Given a string s, return the longest palindromic substring in s.  


### Example 1:
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

### Solution: 
```python
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return s
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return 2
            else:
                return 1
        ans = ""
        # because in two the same word contunue, will have no middle word
        # so add # in between all word
        s = '#'+"#".join(list(s))+'#'
        # init all starter counter
        counter = [0] * (len(s)-2)
        
        for i in range(1, len(s)-1):
            for j in range(1, min(i, (len(s)-1)-i)+1):
                if s[i] != s[i-1] and s[i] != s[i+1] or s[i] == s[i-1] and s[i] == s[i+1]:
                    # if sysmetric
                    if s[i-j] == s[i+j]:
                        # set new max leght on this star word
                        counter[i-1] = 2*j + 1
                    else:
                        break
                else:
                    new_s = s[:i] + s[i+1:]
                    counter[i-1] = 1 + 1
                    if i-j > 0 and i+j < len(new_s)-1 and new_s[i-j] == new_s[i+j]:
                        counter[i-1] = 2*j + 1 + 1
                    else:
                        break
        m = max(counter)
        # find the max length of the start word
        for i, c in enumerate(counter):
            if c == m:
                a = (i+1, c)
                break
        ans_len = c // 2
        ans = s[a[0] - ans_len: a[0] + ans_len + 1]
        # take out # 
        return ans.replace('#', "")
```