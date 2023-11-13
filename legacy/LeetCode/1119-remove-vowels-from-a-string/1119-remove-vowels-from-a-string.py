class Solution:
    def removeVowels(self, s: str) -> str:
        # output string
        output_s = ""
        
        for c in s:
            if c not in ['a','e','i','o','u']:
                output_s += c

        return output_s