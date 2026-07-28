class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        maximum = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maximum = max(prices[r] - prices[l], maximum)
            else:
                l = r
            r += 1
        

        return maximum
            













