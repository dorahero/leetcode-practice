- Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

- A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

### Example 1:
```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

### Example 2:
```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

### Solution: 
```python
class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        k = 0
        self.backtrack(s,ans,k,'')
        return ans



    def backtrack(self, s, ans,k, temp=''):
        if k==4 and len(s)==0:
            # if get 4 numbers
            ans.append(temp[:-1])
            return
        if k==4 or len(s)==0:
            # if get 4 numbers for IP, but still remain some numbers unused
            # or all number be used, but not get 4 number for IP 
            return

        for i in range(3):
            if k>4 or i+1>len(s):
                break

            if int(s[:i+1])>255:
                continue
            # if the number is start with 0 and not '0'
            if i != 0 and s[0]=='0':
                continue
            # remain string, ans, checker, temp IP
            self.backtrack(s[i+1:], ans, k+1, temp+s[:i+1]+'.')
```