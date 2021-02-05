class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        n = len(candidates)
        candidates = sorted(candidates)
        def dfs(cur, cur_sum, idx):                       # consider all case
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target, return and continue next for loop
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n): 
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans        

if __name__ == "__main__":
    candidates = [2,7,6,3,5,1]
    target = 9
    res = Solution().combinationSum(candidates, target)
    print(res)