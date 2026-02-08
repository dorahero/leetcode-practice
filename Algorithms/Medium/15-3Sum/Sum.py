class Solution(object):
    def threeSum(self, nums):
        def two_sum(arr, target):
            l, r = 0, len(arr) - 1
            other_two = set()
            while l < r:
                if arr[l] + arr[r] > target:
                    r -= 1
                elif arr[l] + arr[r] < target:
                    l += 1
                else:
                    tmp = (arr[l], arr[r])
                    l += 1
                    r -= 1
                    other_two.add(tmp)
            return other_two
        nums.sort()
        n = len(nums)
        ans = []
        if len(nums) < 3 or nums[0] > 0:
            return ans 
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                diff = 0 - nums[i]
                two_sum_ok = two_sum(nums[i+1:], diff)
                for t in two_sum_ok:
                    ans.append([nums[i], t[0], t[1]])
            
        return ans
if __name__ == "__main__":
    res = Solution().threeSum([-1,0,1,2,-1,-4])
    print(res)