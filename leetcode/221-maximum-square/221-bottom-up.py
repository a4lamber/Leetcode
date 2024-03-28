class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 状态定义: 
        # -------------------------------------------
        # dp[i][j]: what's the maximum side length of the square
        # can ever be formed with cell[i][j] as the bottom right corner cell
        # state-transition function:
        # -----------------------------------------
        # dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + matrix[i][j]

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        matrix = [[int(element) for element in sublist] for sublist in matrix]

        max_side_length = 0        
        for i in range(m):
            for j in range(n):
                if m == 0 or n == 0:
                    # 1st row or column, initialize
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    # nodes excluding 1st row and column
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1],dp[i][j-1]) + matrix[i][j]
                else:
                    # do nothing
                    pass
                # keep track of max length
                max_side_length = max(max_side_length,dp[i][j])

        return max_side_length * max_side_length
        
        
        
        
        
        
