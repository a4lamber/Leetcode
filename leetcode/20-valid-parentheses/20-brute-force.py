"""
brute force solution, i have done it once on code war,

time complexity: O(n^2), 假设我们的string s长度为n，
作为一个valid parathenes, 里面有n/2 pair of bracket, 
我们需要traverse至少 n/2遍 of length n, 所以时间复杂度为n^2

space complexity: O(1)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = "()"
        curlyBracket = "{}"
        squareBracket = "[]"

        while parentheses in s or curlyBracket in s or squareBracket in s:
            if parentheses in s:
                s = s.replace(parentheses,"")
            if curlyBracket in s:
                s = s.replace(curlyBracket,"")
            if squareBracket in s:
                s = s.replace(squareBracket,"")


        if s is "":
            return True
        else:
            return False
