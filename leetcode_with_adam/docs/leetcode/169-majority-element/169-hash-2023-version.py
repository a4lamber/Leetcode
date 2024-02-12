"""
 # @ Author: Your name
 # @ Description: 2023-02年刷的时候的代码，非常不clean.
 """


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1

        for key, frequency in hashTable.items():
            if frequency > len(nums) // 2:
                return key
