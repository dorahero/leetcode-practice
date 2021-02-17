class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    _ = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = _
        return nums

if __name__ == '__main__':
    res = Solution().sortColors([2,0,2,1,1,0])
    print(res)  