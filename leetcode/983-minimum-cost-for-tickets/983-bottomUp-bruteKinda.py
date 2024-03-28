class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # problem is like climbing stairs but with more options
        # brute force will be 365 days of 1 and 0s
        # DP[i]: minimum cost you have to pay for traveling till brute_days[i]

        days = set(days)
        dp = [0 for _ in range(366)]

        for i in range(1,366):
            if i in days:
                dp[i] = min(dp[max(i-1,0)] + costs[0],dp[max(i-7,0)] + costs[1],dp[max(i-30,0)] + costs[2],)
            else:
                dp[i] = dp[i-1]
        return dp[-1]

            

        

