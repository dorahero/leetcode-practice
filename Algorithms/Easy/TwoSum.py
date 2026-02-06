from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__=="__main__":
    solution = Solution()
    test = [2,7,11,15]
    target = 9
    res = solution.twoSum(test, target)
    print(res)
    test = [2,3,4]
    target = 6
    res = solution.twoSum(test, target)
    print(res)