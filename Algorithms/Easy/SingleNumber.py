from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = set()
        for i in range(0, len(nums)):
            if nums[i] in ans:
                ans.remove(nums[i])
            else:
                ans.add(nums[i])
        return ans.pop()

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    nums1 = [2,2,1]
    print(f"Test 1: {solution.singleNumber(nums1)}") 
    
    # 測試案例 2
    nums2 = [4,1,2,1,2]
    print(f"Test 2: {solution.singleNumber(nums2)}")