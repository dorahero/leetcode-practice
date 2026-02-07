import env
from Algorithms.function.TreeComponent import create_tree, print_tree
class Solution:
    def isSymmetric(self, root) -> bool:
        def valid(left, right):
            if not left and not right:
                return True
            elif not left:
                return False
            elif not right:
                return False
            elif left.val != right.val:
                return False
            return valid(left.left, right.right) and valid(left.right, right.left)
        left = root.left
        right = root.right
        return valid(left, right)

        
def main():
    root = create_tree([1,2,2,None,3,None,3])
    print_tree(root)
    solution = Solution()
    print(solution.isSymmetric(root))

if __name__ == '__main__':
    main()