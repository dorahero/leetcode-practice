from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    nums1 = [1,2,3,1]
    print(f"Test 1: {solution.containsDuplicate(nums1)}") 
    
    # 測試案例 2
    nums2 = [1,2,3,4]
    print(f"Test 2: {solution.containsDuplicate(nums2)}")