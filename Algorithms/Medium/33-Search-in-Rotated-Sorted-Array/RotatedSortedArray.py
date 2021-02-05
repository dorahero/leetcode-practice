class Solution(object):
    def search(self, nums, target):
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
if __name__ == "__main__":
    res = Solution().search([4,5,6,7,0,1,2], 0)
    print(res)