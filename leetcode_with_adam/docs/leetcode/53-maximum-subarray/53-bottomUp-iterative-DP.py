class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm (iterative bottom up DP)
        # DP[i]: 以i为终点的maximum subarray
        if len(nums) == 1: return nums[0]
        
        # initialize DP
        currentMax = nums[0]
        globalMax = nums[0]

        for i in range(1,len(nums)):

            # throw away subarray if accumulative sum is nagative
            if nums[i] > currentMax + nums[i]: #说明currentMax为负数，只有负面效果，舍弃
                currentMax = nums[i]
            else:
                currentMax = currentMax + nums[i]

            if globalMax < currentMax:
                globalMax = currentMax
        
        return globalMax
