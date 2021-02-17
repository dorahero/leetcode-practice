class Solution(object):
    def subsets(self, nums):
        def backtracking(r, res, ne):
            if r == 0:
                ans.append(res[:])
            else:
                for i in range(ne, n):
                    res.append(nums[i])
                    backtracking(r-1, res, i+1)
                    res.pop()
        ans = [[]]
        n = len(nums)
        for k in range(1, n+1):
            backtracking(k, [], 0)
        return ans

if __name__ == '__main__':
    res = Solution().subsets([1,2,3])
    print(res)  