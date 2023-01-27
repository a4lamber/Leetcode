"""
Condition:
- You may not use the same element twice
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare a hashmap
        hashmap = {}
        # initialize the hashmap with key-value pair
        """
        Example:
        nums = [5,1,9,10]
        saves in the form of {value:index}
        hashmap = {
            5: 0,
            1:1,
            9:2,
            10:3
        }
        """
        for i in range(len(nums)):
            # value to be key, index be value
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            # calculate the condtion needs to be met
            condition = target - nums[i]
            # check both conditions
            # check 为了met condition的条件是否存在于hash中，以及hash是否等于其本身
            if condition in hashmap and hashmap[condition] != i:
                return [i,hashmap[condition]]

