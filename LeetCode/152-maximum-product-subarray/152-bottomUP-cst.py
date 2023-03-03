class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 难点: 数列中的负数或0, 负数可以通过track minimum so far来解决，0可以通过
        # DP:
            # max_so_far[i]: maximum product ending on nums[i]
            # min_so_far[i]: minimum product ending on nums[i]. Acts as a fail-safe for array with odd number of negative numbers
        
        if len(nums) == 1: return nums[0]

        max_prev = nums[0]
        min_prev = nums[0]
        
        global_max = nums[0]

        for i in range(1,len(nums)):
            min_temp = min_prev
            max_temp = max_prev

            max_prev = max(nums[i], min_temp * nums[i], max_temp * nums[i])
            min_prev = min(nums[i], min_temp * nums[i], max_temp * nums[i])

            if max_prev > global_max: global_max = max_prev

        
        return global_max



        
        
            
        

        

        



