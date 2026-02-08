class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        dict = {')':'(', ']':'[', '}':'{'} 
        for char in s: 
            if char in dict.values(): 
                stack.append(char) # to pair
            elif char in dict.keys(): 
                if stack==[] or stack.pop()!=dict[char]: # if pair remove, last must need pair with cur
                    return False 
            else: 
                return False 
        return stack==[] 

solution = Solution()
s = "()"
print(solution.isValid(s))