### Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Constraints:
- 0 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.

### Solution: 
```python
import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        # only use min(str) to compare max(str)
        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1      
```