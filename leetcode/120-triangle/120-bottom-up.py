class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # initial condition
        # dp[i][j]: the minimum path sum falling to that position
        # state transition function:
        # O(n^2) in space for storing dp, O(n^2) in time for 1 + 2 + 3 + 4 + ... + n

        n = len(triangle)
        dp = [[0] * i for i in range(1,n+1)]
        
        # edge cases
        if n == 1: return triangle[0][0]

        dp[0][0] = triangle[0][0]

        # scan vertically
        for i in range(1,n):
            # scan each row
            for j in range(len(triangle[i])):
                # boundary nodes:
                # 1. coming from top only (1st element)
                # 2. coming from top left only (last element)
                # interior nodes:
                # 3. coming from top and top left
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                    continue
                
                if j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    continue
                
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1])




