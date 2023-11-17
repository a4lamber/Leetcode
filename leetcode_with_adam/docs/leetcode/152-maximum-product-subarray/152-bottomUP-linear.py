class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 难点: 数列中的负数或0, 负数可以通过track minimum so far来解决，0可以通过
        # DP:
            # max_so_far[i]: maximum product ending on nums[i]
            # min_so_far[i]: minimum product ending on nums[i]. Acts as a fail-safe for array with odd number of negative numbers
        
        if len(nums) == 1: return nums[0]

        max_so_far = [None for _ in range(len(nums))]
        min_so_far = [None for _ in range(len(nums))]

        max_so_far[0] = nums[0]
        min_so_far[0] = nums[0]

        for i in range(1,len(nums)):
            max_so_far[i] = max(max_so_far[i-1] * nums[i],min_so_far[i-1] * nums[i],nums[i])
            min_so_far[i] = min(max_so_far[i-1] * nums[i],min_so_far[i-1] * nums[i],nums[i])
        
        return max(max_so_far)
        
        
        
        
            
        

        

        




