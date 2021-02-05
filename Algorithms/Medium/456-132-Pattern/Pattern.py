class Solution:
    def find132pattern(self, nums):
        if len(nums) <=2:
            return False
        # lowerbound
        third = float('-inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            # first < second
            if nums[i] < third:
                return True
            else:
                # third < second
                while stack and stack[-1] < nums[i]:
                    third = stack.pop()
            stack.append(nums[i])
        return False
if __name__ == "__main__":
    res = Solution().find132pattern([3,5,0,3,4])