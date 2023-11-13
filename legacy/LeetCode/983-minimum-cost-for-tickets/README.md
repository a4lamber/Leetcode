# Approach 1 Bottom up linear

- `base case:` It doesn't have a base case for this problem
- `initialization:` Just initialize it to zeros for all.
- `DP[i] definition`: naively generate a rolling
- `transition function:` 




A couple of key takeaway for this problem:
- this problem uses the "brute-ish" DP jerry was telling me about. It is going to make things easier.
- it doesn't matter how large you set you `DP array` is as long as you are covering all the solution
- don't be too dependent on `list()` and please use more `defaultdict` or `set`




```python
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
```