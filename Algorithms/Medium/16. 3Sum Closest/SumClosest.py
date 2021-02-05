class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        n = len(nums)
        closest_diff = float('Inf')
        res = []
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                tmp = [nums[i], nums[l], nums[r]]
                sum_tmp = sum(tmp)
                _ = sum_tmp - target
                if abs(_) < closest_diff:
                    res = tmp
                    closest_diff = abs(_)
                if _ == 0:
                    return sum(res)
                elif _ < 0:
                    l += 1
                elif _ > 0:
                    r -= 1
        return sum(res)
        
if __name__=="__main__":
    res = Solution().threeSumClosest([0,2,1,-3], 1)
    print(res)