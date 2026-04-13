class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # return the maximum profit, the big difference
        # brute force
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        
        # return max_profit

        # Two pointer

        l,r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1
        
        return maxP
