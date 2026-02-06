import env 

from Algorithms.function.TreeComponent import TreeNode, create_tree, print_tree
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

def main():
    print("Testing create_tree and print_tree with [1, 2, 3, None, 4]")
    values = [1, 2, 3, None, 4]
    root = create_tree(values)
    print_tree(root)
    
    solution = Solution()

    print(solution.maxDepth(root))
    print("\nTesting create_tree and print_tree with [1, 2, 3, 4, 5, 6, 7]")
    values = [1, 2, 3, 4, 5, 6, 7]
    root = create_tree(values)
    print_tree(root)

    print(solution.maxDepth(root))


if __name__ == "__main__":
    main()
