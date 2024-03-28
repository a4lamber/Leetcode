class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window approach O(n) in time, O(1) in space
        
        # two 
        min_price = float('inf')
        max_difference = 0

        # not gonna buy on last day
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_difference:
                max_difference = prices[i] - min_price
        
        return max_difference
            

            
