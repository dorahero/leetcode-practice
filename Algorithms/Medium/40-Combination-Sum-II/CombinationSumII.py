class Solution(object):
    def combinationSum2(self, candidates, target):
        def backtrack(nums,targetLeft,path):
            if targetLeft==0:
                ans.append(path)
                return
            
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if nums[i]>targetLeft:
                    break
                backtrack(nums[i+1:],targetLeft-nums[i],path+[nums[i]])    
        ans = []
        backtrack(sorted(candidates), target, [])
        return ans
if __name__ == "__main__":
    res = Solution().combinationSum2([10,1,2,7,6,1,5], 8)
    print(res)