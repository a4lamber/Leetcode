class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] number of possible ways to get here
        
        # edge case
        if m == 1 or n == 1: return 1

        # initialize the dp array
        dp = [[ 0 for j in range(n)] for i in range(m)]

        for i in range(n):
            dp[0][i] = 1
        
        for j in range(m):
            dp[j][0] = 1
        
        # horizontal scanning
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
  
              
        
