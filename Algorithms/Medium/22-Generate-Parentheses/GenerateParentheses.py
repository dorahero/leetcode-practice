class Solution:
  def generateParenthesis(self, n):
    ans = []
    
    queue = []
    queue.append(['(', n-1, n]) # node = ['parentheses', number of left, number of right]
    
    while queue:
      node = queue.pop(0)
      
      if node[1] >= 1: # If there are still left
        queue.append([node[0]+'(', node[1]-1, node[2]]) # Add 1 '(', then number of '(' minus 1
        
      if node[2] > node[1]: # means there is at least one '(' to pair with ')'
        queue.append([node[0]+')', node[1], node[2]-1]) # Add 1 ')', then number of ')' minus 1
        
      if node[1] == node[2] == 0: # if no '(' and ')' append result 
        ans.append(node[0])
        
    return ans
if __name__ == "__main__":
    res = Solution().generateParenthesis(2)
    print(res)