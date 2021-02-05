class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            nums.reverse()
            return nums
        _ = sorted(nums)
        _.reverse()
        # if nums is the max permutation
        if nums == _:
            nums.reverse()
            return nums
        # find the max index of the Strictly increasing number 5 1 3 1 6 2 '5' 3
        x = max(i for i in range(1, len(nums)) if nums[i - 1] < nums[i])
        # find the max index of the number which bigger than the number which index is x-1, 5 1 3 1 6 2 5 '3'
        y = max(j for j in range(x, len(nums)) if nums[j] > nums[x - 1])
        # switch with the number which index is x-1, 5 1 3 1 6 '3' 5 '2' 
        nums[y], nums[x - 1] = nums[x - 1], nums[y]
        # and reverse the other number
        # becuse they must be decreasing 
        nums[x:] = reversed(nums[x:])
        return nums
        
        
if __name__ == "__main__":
    nums = [5,1,3,1,6,7,4,3]
    res = Solution().nextPermutation(nums)
    print(res)