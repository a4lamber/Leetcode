class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] the min path sum reach cell[i][j]
        n = len(matrix)
        
        # edge case
        if n == 1: return matrix[0][0]

        dp = [[0 for j in range(n)] for i in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # scan vertical
        for i in range(1,n):
            # scan horizontally
            for j in range(n):
                # left boundary nodes
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                    continue

                # right bounday nodes
                if j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j])
                    continue

                # interior nodes
                dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        
        return min(dp[-1])
                
        
