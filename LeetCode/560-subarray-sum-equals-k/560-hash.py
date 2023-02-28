class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash key-value pair
        # any particular sum: how many times it happens
        count = 0
        prefixSum = 0
        prefixSumHash = {0:1} # initialze {0,1}, 来计算那些num[i]==k的情况

        for i in range(0,len(nums)):
            # update sum
            prefixSum += nums[i]
            # check if target in it (思路很像two sum)
            diff = prefixSum - k
            if diff in prefixSumHash:
                count += prefixSumHash[diff]
            
            if prefixSum in prefixSumHash:
                prefixSumHash[prefixSum] += 1
            else:
                prefixSumHash[prefixSum] = 1
            
        return count

        
