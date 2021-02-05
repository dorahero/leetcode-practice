- In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.  

- What if we change the game so that players cannot re-use integers?  

- For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.  

- Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise return false. Assume both players play optimally.  

### Solution: 
```python
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal == 0:
            return True
        self.max = maxChoosableInteger
        self.d = {}
        
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger+1) // 2:
            return False
        
        return self.recursion(2**maxChoosableInteger-1, desiredTotal)
        
    
    def recursion(self, mask, total):  #bit 'set' means still not chosen 
        
        if mask >= 2**(total-1):
            return True
        if mask in self.d:
            return self.d[mask]
        
        for i in range(self.max):
            if mask & (1<<i):  #if the ith bit is set
                newmask = mask & ~(1<<i)  #unset the ith bit
                if self.recursion(newmask, total-i-1) == False:
                    self.d[mask] = True
                    return True
        self.d[mask] = False
        return False
```