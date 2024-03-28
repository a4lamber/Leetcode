class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev = prevPrev =0

        for i in range(2,len(cost)+1):
            temp = prev
            prev = min(prev + cost[i-1], prevPrev + cost[i-2])
            prevPrev = temp
        
        return prev



