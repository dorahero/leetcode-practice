import env
from Algorithms.function.TreeComponent import create_tree, print_tree
class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, minmum, maximum):
            if not node:
                return True
            if minmum >= node.val or maximum <= node.val:
                return False
            return valid(node.left, minmum, node.val) and valid(node.right, node.val, maximum)
        return valid(root, float("-inf"), float("inf"))

def main():
    root = create_tree([2, 1, 3])
    print_tree(root)
    solution = Solution()
    print(solution.isValidBST(root))

if __name__ == '__main__':
    main()