from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2[:]
        # nums1.sort()

        midx = m - 1 # m last
        nidx = n - 1
        right = m + n - 1 # all last

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            right -= 1

def main():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()