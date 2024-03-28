class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        curr_profit = 0
        for i in range(1,len(prices)):
            curr_profit = prices[i] - prices[i-1] 
            if curr_profit > 0:
                total_profit += curr_profit
        
        return total_profit
 
