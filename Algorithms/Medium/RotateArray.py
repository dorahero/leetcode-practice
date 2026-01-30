from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 確保 k 不會超過陣列長度
        
        nums[:] = nums[n-k:] + nums[:n-k]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(f"Test 1: {nums1}") # Expected: [5, 6, 7, 1, 2, 3, 4]
    
    # 測試案例 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(f"Test 2: {nums2}") # Expected: [3, 99, -1, -100]