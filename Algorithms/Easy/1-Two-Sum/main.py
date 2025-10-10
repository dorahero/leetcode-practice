class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if target == nums[i] + nums[j+i+1]:
                    return [i, j+i+1]
        return None

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  