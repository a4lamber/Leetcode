class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # DP bottom up
        # DP[i] 以i为结尾的subarray的最大值
        counter = 0
        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    counter += 1
        return counter
