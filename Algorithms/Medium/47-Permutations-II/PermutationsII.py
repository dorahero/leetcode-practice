class Solution(object):
    def permuteUnique(self, nums):
        def nextNum(n):
            array = n[:]
            i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
            j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
            array[j], array[i - 1] = array[i - 1], array[j]
            array[i:] = reversed(array[i:])
            return array

        def factorial(n):
            r = 1
            for i in range(1, n+1):
                r *= i
            return r

        _ = {str(x): 0 for x in nums}
        for n in nums:
            _[str(n)] += 1
        # counter : total permutation number
        counter = 1
        for i in range(1, len(nums)+1):
            counter *= i
        for d in _:
            counter /= factorial(_[d])
        ans = []
        nums = sorted(nums)
        ans.append(nums)
        # find next bigger number
        for j in range(int(counter)-1):
            nums  = nextNum(nums)
            ans.append(nums)

        return ans

if __name__=="__main__":
    res = Solution().permuteUnique([1,1,2])
    print(res)
        