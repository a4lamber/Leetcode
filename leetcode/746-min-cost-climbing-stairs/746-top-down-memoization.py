class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recursion + memoization, 用这个思路实际上就很像斐波那契数列了
        
        def minimum_cost(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]
            
            down_one = cost[i-1] + minimum_cost(i-1)
            down_two = cost[i-2] + minimum_cost(i-2)
            memo[i] = min(down_one, down_two)
            return memo[i]
        
        memo = {}
        return minimum_cost(len(cost))


