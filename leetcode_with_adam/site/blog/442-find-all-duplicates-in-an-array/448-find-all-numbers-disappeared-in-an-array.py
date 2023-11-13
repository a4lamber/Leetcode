"""
each integer appears once or twice.
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # declare a hash and output
        hashtable = {}
        output = []

        # one-pass hash
        for i in range(len(nums)):
            # check if current element in the hash 
            if nums[i] in hashtable:
                # append to output
                output.append(nums[i])
            # assign value to hash
            hashtable[nums[i]] = i 
        
        return output