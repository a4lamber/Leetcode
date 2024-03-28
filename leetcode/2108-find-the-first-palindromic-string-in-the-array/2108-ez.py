class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def checkPalindrome(candidateString):
            left = 0
            right = len(candidateString) - 1

            while left < right:
                if candidateString[left] != candidateString[right]:
                    return False
                left += 1
                right -= 1

            return True


        for word in words:
            if checkPalindrome(word):
                return word

        
        return ""