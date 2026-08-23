class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        return max(profit, 0)
            