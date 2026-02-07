from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        tmpMaxSum = 0
        for n in nums:
            if tmpMaxSum < 0:
                tmpMaxSum = 0
            
            tmpMaxSum += n
            maxSum = max(tmpMaxSum, maxSum)
        
        return maxSum
    

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(nums))

if __name__ == "__main__":
    main()