class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize an dp list
        dp = list()

        if len(nums) == 0: 
            return 0
        
        dp.append(nums[0])
        if len(nums) == 1:
            return dp[0]
        
        dp.append(max(nums[0],nums[1]))
        if len(nums) == 2:
            return dp[1]

        
        for i in range(2,len(nums)):
            # robber has two choices:
            # Option1: 偷房子i
            # Option2: 不偷房子i, 因为[i-1]的值更大，而且i+1>= 0, 所以这么偷不会亏
            dp.append(max(dp[i-1], dp[i-2] + nums[i]))
        
        return dp[-1]


