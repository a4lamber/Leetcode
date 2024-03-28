class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 思路：
        # array = minimum sum subarray + maximum sum subarray
        # currentMaxDp[i] : ending on element i
        # currentMinDp[i]
        # Bottom up, linear solution

        currentMaxDp = [None for _ in range(len(nums))]
        currentMinDp = [None for _ in range(len(nums))]

        currentMaxDp[0] = currentMinDp[0] = nums[0]

        for i in range(1,len(nums)):
            currentMaxDp[i] = max(nums[i],nums[i] + currentMaxDp[i-1])
            currentMinDp[i] = min(nums[i],nums[i] + currentMinDp[i-1])
        
        globalMax = max(currentMaxDp)
        globalMin = min(currentMinDp)

        # consider edge cases of all zeros
        if globalMax < 0:
            # all negative
            return globalMax
        else:
            return max(sum(nums) - globalMin, globalMax)

  

        


