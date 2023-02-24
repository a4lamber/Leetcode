class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: # 没有
            return 0

        if len(nums) == 1:# 有一个house
            return nums[0]
        
        if len(nums) == 2: # 有两个houses
            return max(nums[0],nums[1])
        
        # > 2 houses, we need to cover all cases
        res1 = self.helper(nums,0,len(nums)-1)
        res2 = self.helper(nums,1,len(nums))

        return max(res1,res2)

    
    def helper(self,nums,start,end):
        # return maximum amount of house robber I 
        dp = []
        
        dp.append(nums[start])
        if start == end:
            return nums[start]
        
        dp.append(max(nums[start],nums[start + 1]))
        if end - start == 1:
            return dp[-1]
        
        dpLength = end - start 
    
        # general cases, end - start>= 2, 也就是至少三个数
        for i in range(2, dpLength):
            dp.append(max(dp[i-1], dp[i-2] + nums[start + i]))
        
        # return the last index
        return dp[-1]


