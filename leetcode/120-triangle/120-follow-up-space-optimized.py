class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # create an array of size 2xn
        n = len(triangle)
        dp = [[0] * n for i in range(1,3)] 

        # for 1st row
        dp[0][0] = triangle[0][0]

        # scan vertiacally
        for i in range(1,n):
            for j in range(i+1):
                # left boundary
                if j == 0:
                    dp[1][j] = triangle[i][j] + dp[0][j]
                    continue

                # right bounday
                if j == i:
                    dp[1][j] = triangle[i][j] + dp[0][j-1]
                    continue

                dp[1][j] = triangle[i][j] + min(dp[0][j-1],dp[0][j])

            # end of this row, let's swap
            dp = [dp[1],dp[0]]
        
        # result in first row since we swapped
        return min(dp[0])

