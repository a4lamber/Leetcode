class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 其实这一题很像大富翁，要避开收费最多的旅馆
        # bottom up tabulation approach

        # initialize dp, with extra 1 space for storing "top of the floor"
        minimum_cost = [0 for _ in range(len(cost) + 1)]

        
        for i in range(2,len(cost) + 1):
            take_one_step = minimum_cost[i-1] + cost[i-1] # 走一步到2
            take_two_step = minimum_cost[i-2] + cost[i-2] # 走两步到2
            # 每一步都想象成最后一步
            minimum_cost[i] = min(take_one_step,take_two_step)

        return minimum_cost[len(cost)]



