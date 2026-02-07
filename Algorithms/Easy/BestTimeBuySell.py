from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for p in prices:
            if buy > p:
                buy = p
            profit = max(profit, p - buy)
        
        return profit
        
def main():
    prices = [2,4,1]
    solution = Solution()
    print(solution.maxProfit(prices))

if __name__ == "__main__":
    main()