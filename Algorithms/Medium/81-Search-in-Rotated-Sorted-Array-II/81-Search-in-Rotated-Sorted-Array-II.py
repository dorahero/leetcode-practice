class Solution(object):
    def search(self, nums, target):
        ans = False
        if target in nums:
            ans = True
        return ans
        

if __name__ == '__main__':
    res = Solution().search(nums = [2,5,6,0,0,1,2], target = 3)
    print(res)  