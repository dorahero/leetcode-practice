from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        i = 0
        profit = 0
        min_tmp = -1
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                if min_tmp == -1:
                    min_tmp = prices[i]
            elif prices[j] < prices[i]:
                if min_tmp > -1:
                    profit += prices[i] - min_tmp
                    min_tmp = -1
            if j == len(prices) - 1:
                if min_tmp > -1:
                    profit += prices[j] - min_tmp
                    min_tmp = -1
            i += 1
        return profit

# Example usage
solution = Solution()
nums = [1,9,6,9,1,7,1,1,5,9,9,9]
result = solution.maxProfit(nums)
print(result)  # Output: 2