class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute force: calculates every subarray and sum O(n^3)
        counter = 0

        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                if sum(nums[i:j]) == k:
                    counter += 1
        
        return counter
