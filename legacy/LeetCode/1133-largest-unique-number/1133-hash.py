class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        valueHash = {}

        for num in nums:
            if num not in valueHash.keys():
                valueHash[num] = 1
            else:
                valueHash[num] += 1

        maxNumber = -1

        for key, occurance in valueHash.items():
            if occurance == 1 and key > maxNumber:
                maxNumber = key

        return maxNumber

                