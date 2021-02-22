class Solution(object):
    def subsetsWithDup(self, nums):
        def backtracking(r, res, ne):
            print(res)
            print(r)
            if r == 0 and res[:] not in ans:
                ans.append(res[:])
            else:
                for i in range(ne, n):
                    res.append(nums[i])
                    backtracking(r-1, res, i+1)
                    res.pop()
        ans = [[]]
        n = len(nums)
        nums = sorted(nums)
        for k in range(1, n+1):
            # C n choose k
            # k, start list, counter
            backtracking(k, [], 0)
        return ans

if __name__ == '__main__':
    res = Solution().subsetsWithDup(nums = [1,2,2])
    print(res)  