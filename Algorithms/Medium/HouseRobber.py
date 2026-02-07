from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = maxRob = 0
        
        for cur in nums:
            tmp = max(maxRob, prev + cur)
            prev = maxRob
            maxRob = tmp
        
        return maxRob

def main():
    nums = [2,4,8,9,9,3]
    solution = Solution()
    print(solution.rob(nums))

if __name__ == "__main__":
    main()