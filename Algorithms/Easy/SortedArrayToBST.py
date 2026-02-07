import env
from Algorithms.function.TreeComponent import print_tree, TreeNode
from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if not nums:
            return None
        
        # small to left
        n = len(nums) // 2
        root = TreeNode(nums[n])

        root.left = self.sortedArrayToBST(nums[:n])
        root.right = self.sortedArrayToBST(nums[n+1:])

        return root


def main():
    nums = [-10,-3,0,5,9]
    solution = Solution()
    print_tree(solution.sortedArrayToBST(nums))

if __name__ == '__main__':
    main()