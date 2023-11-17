class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp: minimum value to reach this grid
        # constrain: information flows from top or left

        m = len(grid)
        n = len(grid[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        dp[0][0] = grid[0][0]

        # initialize the dp
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]

