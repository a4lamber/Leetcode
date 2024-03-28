class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # LIS[i]: longest increasing sequence ending on nums[i]
        # count[i]: number of LIS ending on nums[i]
        # base case: all one
        LIS = [1 for num in nums]
        count = [1 for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[i] < LIS[j] + 1: # find a longer sequence
                        LIS[i] = LIS[j] + 1
                        count[i] = count[j]
                        continue
                        
                    if LIS[i] == LIS[j] + 1: # find another sequence with same length
                        LIS[i] = LIS[j] + 1
                        count[i] += count[j]
        # update the data 
        max_length = max(LIS)
        return sum(c for l, c in zip(LIS, count) if l == max_length)




