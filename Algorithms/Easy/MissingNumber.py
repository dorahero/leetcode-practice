from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = n * (n+1) // 2
        t_sum_n = sum(nums)
        return sum_n - t_sum_n

solution = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(nums))