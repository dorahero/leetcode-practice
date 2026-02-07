# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import env
from Algorithms.function.TestComponent import isBadVersion
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


def main():
    n = 2126753390
    solution = Solution()
    
    print(solution.firstBadVersion(n))

if __name__ == '__main__':
    main()