class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Rroblem:    palindrom or palindrom after removing at most one character
        # edge cases: any two characters string like "aa"
        #             any string consists of only one character "aaaaa"
        #              
        # brute force: 
        #           1. check validPalindrome, O(n)
        #           2. remove one character, O(m)
        # 

        # helper function for palindrom
        def checkPalindrome(s):
            # this coverse both edge cases "a" or "aa"
            i = 0
            j = len(s) -1

            while i < j:
                if s[i] != s[j]:
                    # find mismatch
                    return False
                i += 1
                j -= 1
            # check till the end
            return True

        # best case scenerio
        if checkPalindrome(s):
            return True


        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # we do the checking, remove left by one or right by one
                return checkPalindrome(s[left:right]) or checkPalindrome(s[left+1:right+1])

            left += 1
            right -= 1

        return False
            

