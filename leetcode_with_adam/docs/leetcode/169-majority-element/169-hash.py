class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1
        
        for key, frequency in hashTable.items():
            if frequency > len(nums)//2:
                return key

