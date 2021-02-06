class Solution(object):
    def permute(self, nums):
        def nextNum(n):
            array = n[:]
            i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
            j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
            array[j], array[i - 1] = array[i - 1], array[j]
            array[i:] = reversed(array[i:])
            return array
        counter = 1
        for i in range(1, len(nums)+1):
            counter *= i
        ans = []
        nums = sorted(nums)
        ans.append(nums)
        for j in range(counter-1):
            nums  = nextNum(nums)
            ans.append(nums)

        return ans
if __name__ == "__main__":
    res = Solution().permute([1,2,3,4,5])
    print(res)