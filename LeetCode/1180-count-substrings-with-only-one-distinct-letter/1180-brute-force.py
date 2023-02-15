def accumulativeSum(n):
    return int(n * (n+1)/2)

class Solution:
    def countLetters(self, s: str) -> int:


        left = 0
        right = 0
        total = 0
        
        for right in range(len(s) + 1):
            # change of variable or out of index
            if right == len(s) or s[left] != s[right]:
                len_substring = right - left
        
                total += (1 + len_substring) * len_substring // 2
                left = right
        return total
