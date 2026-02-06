from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) < 1:
            return
        addFirst = True
        for i in range(1, len(digits)+1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                addFirst = False
                break
        if addFirst:
            digits = [1] + digits
        return digits

if __name__=="__main__":
    solution = Solution()
    test1 = ([9])
    res = solution.plusOne(test1)
    print(res)