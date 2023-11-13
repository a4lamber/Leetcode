class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        # traverse the list, O(n)
        for num in nums:
            if num not in hashmap.keys():
                # if it's not in, initialize it to be zero
                hashmap[num] = 1
            else:
                # if it's in, add one occurence
                hashmap[num] += 1

        # traver the hash to see what's value is equal to one, O(n)
        for key in hashmap.keys():
            # find the key only occurs once
            if hashmap[key] == 1:
                return key
            
                
            

        
            
