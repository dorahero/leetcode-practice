from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        for i in range(0, len(nums)):  
            for j in range(i+1, len(nums)):
                if nums[i] == 0:
                    nums[i] = nums[j]
                    nums[j] = 0

if __name__=="__main__":
    solution = Solution()
    test1 = [0,1,0,3,12]
    solution.moveZeroes(test1)
    print(test1)
    test2 = [0]
    solution.moveZeroes(test2)
    print(test2)