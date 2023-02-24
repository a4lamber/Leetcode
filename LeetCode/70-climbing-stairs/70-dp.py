class Solution:
    def climbStairs(self, n: int) -> int:
        # only allow to climb one or two stairs, count all distint ways
        # 1 <= n <= 45
        dp = list()

        if n == 1: return 1
        if n == 2: return 2
        
        dp.append(1)
        dp.append(2)

        # 从第三个case开始, 也就是index = 2 
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[-1]

        
