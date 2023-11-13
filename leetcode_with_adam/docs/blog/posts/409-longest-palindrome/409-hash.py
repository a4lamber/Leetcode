class Solution:
    def longestPalindrome(self, s: str) -> int:
        # intuiton hash to mark down frequencies
        # maximum one unique 
        
        # edge cases
        # if len(set(s)) == 1:
        #     return len(s) 
        
        
        characterHash = {}

        for char in s:
            if char not in characterHash.keys():
                characterHash[char] = 1
            else:
                characterHash[char] += 1
        
        longestLength = 0
        numberOfSingleCharacter = 0

        for key,value in characterHash.items():
            # character appearas even times
            if value % 2 == 0:
                longestLength += value
            

            # characters appears odd time 
            if value % 2 == 1:
                numberOfSingleCharacter += 1
                longestLength += (value - 1)

        if numberOfSingleCharacter > 0:
            longestLength += 1
        
        return longestLength