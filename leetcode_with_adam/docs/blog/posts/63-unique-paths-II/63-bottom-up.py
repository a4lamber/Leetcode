class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 
List[List[int]]) -> int:
        # analysis:
        # initial condition: As for 1st row or 1st column, if 
we see one obstable, the rest of the row and column would be 
zero
        # dp[i][j]: number of ways to get to this grid. If an 
obstable is on the grid, then 0.
        # state transition function: 
        # 
        # (i,j) not an obstabcle   dp[i][j] = dp[i-1]dp[j] + 
dp[i][j-1]
        # (i,j) is an obstable then dp[i][j] = 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # edge cases:
        if obstacleGrid[0][0] == 1: return 0
        if m == 1 and n == 1 and obstacleGrid[0][0] == 0: 
return 1

        
        dp = [[0 for j in range(n)] for i in range(m)]

        # initialize 1st row
        for j in range(1,m):
            if obstacleGrid[j][0] == 1:
                break
            else:
                dp[j][0] = 1
        
        # initialize 1st column
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                # bump into obstacle
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # update dp
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
            
        return dp[-1][-1]

        
