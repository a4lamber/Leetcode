class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # bottom up, constant space
        # DP: 这里track两个信息:
        # current min
        # current max
        
        globalMin = currentMin = nums[0]
        globalMax = currentMax = nums[0]

        for i in range(1,len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            currentMin = min(currentMin + nums[i], nums[i])

            globalMax = max(currentMax,globalMax)
            globalMin = min(currentMin,globalMin)

        
        if globalMax < 0:
            return globalMax
        else:
            return max(globalMax,sum(nums) - globalMin)


            

