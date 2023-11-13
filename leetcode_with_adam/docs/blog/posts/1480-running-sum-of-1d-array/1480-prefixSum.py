class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1: return [nums[0]]
        

        prefixSum = 0
        res = [None for _ in range(len(nums))]

        for i in range(len(nums)):
            prefixSum += nums[i]
            res[i] = prefixSum
        
        return res
