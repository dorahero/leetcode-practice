### Example 1:
```
Input: x = 123
Output: 321
```

### Example 2:
```
Input: x = -123
Output: -321
```

### Constraints:
- -231 <= x <= 231 - 1

### Solution: 
```python
class Solution(object):
    def reverse(self, x):
            if x >= 0:
                a = []
                for i in range(len(str(x))):
                    a.append(x // (10**i) % 10)
                sum = 0
                for i, j in enumerate(a):
                    sum += j*(10**(len(str(x))-1-i))
                Output = sum
                if sum <= 2147483647 and sum >= -2147483648:
                    return Output
                else:
                    return 0
            else:
                x = -x
                a = []
                for i in range(len(str(x))):
                    a.append(x // (10**i) % 10)
                sum = 0
                for i, j in enumerate(a):
                    sum += j*(10**(len(str(x))-1-i))
                Output = -sum
                if sum <= 2147483647 and sum >= -2147483648:
                    return Output
                else:
                    return 0
              
```