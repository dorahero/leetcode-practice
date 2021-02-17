class Solution(object):
    def searchMatrix(self, matrix, target):
        ans = False
        for m in matrix:
            if target in m:
                return True
        return ans

if __name__ == '__main__':
    res = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(res)  