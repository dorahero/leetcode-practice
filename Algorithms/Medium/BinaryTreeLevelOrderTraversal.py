import env
from Algorithms.function.TreeComponent import create_tree, print_tree
from collections import deque
from typing import List
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            sameLevel = []

            for _ in range(len(q)):
                node = q.popleft()
                sameLevel.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(sameLevel)
            
        return res

def main():
    root = create_tree([3,9,20,None,None,15,7])
    print_tree(root)
    solution = Solution()
    print(solution.levelOrder(root))

if __name__ == '__main__':
    main()