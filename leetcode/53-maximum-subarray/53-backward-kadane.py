class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # bottom, constant
        # base cases： DP[-1] = nums[-1]
        # DP[i]： 以nums[i]为开头的maximum maxSubArray
        # transisiton function: DP[i-1] = max(DP[i] + nums[i-1],nums[i-1])
        # USE CONSTANT TIME COMPLEXITY

        if len(nums) == 1: return nums[0]

        currentMax = nums[-1]
        globalMax = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            currentMax = max(nums[i], nums[i] + currentMax)
            globalMax = max(currentMax,globalMax)

        return globalMax
