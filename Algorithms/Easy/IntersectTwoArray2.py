from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(f"Test 1: {solution.intersect(nums1, nums2)}") 
    