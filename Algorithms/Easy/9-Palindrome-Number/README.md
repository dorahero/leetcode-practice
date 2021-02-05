- Given an integer x, return true if x is palindrome integer.  

- An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.  
 
 
### Example 1:
```
Input: x = 121
Output: true
```

### Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Constraints:
- -231 <= x <= 231 - 1

### Solution: 
```python
class Solution(object):
    def isPalindrome(self, x):
            if x >= 0:
                a = []
                for i in range(len(str(x))):
                    a.append(x // (10**i) % 10)
                sum = 0
                for i, j in enumerate(a):
                    sum += j*(10**(len(str(x))-1-i))
                if sum == x:
                    return True
                else:
                    return False
            else:
                return False
```