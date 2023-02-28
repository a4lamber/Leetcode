class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maximum average subarray will have the maximum sum as well
        # so we just use 
        
        currentMax = sum(nums[0:k])
        globalMax = currentMax

        for i in range(k,len(nums)):
            currentMax += nums[i]
            currentMax -= nums[i-k]
            
            globalMax = max(globalMax,currentMax)
        
        return globalMax/k
