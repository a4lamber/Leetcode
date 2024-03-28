class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #
        hashtable = {}

        for i in range(len(nums)):
            # check if current element
            if nums[i] in hashtable.keys():
                return True

            # assign key-value pair as value-index 
            hashtable[nums[i]] = i
        
        return False