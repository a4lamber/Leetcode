class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        res_len = 0 # at least one

        for i in range(len(s)):
            # check for odd
            left,right = i,i
            # under constrain and equal, we expand out
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1
            
            # check for even
            left,right = i,i+1
            # under constrain and equal, we expand out
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_len = right - left + 1
                    res = s[left:right+1]
                left -= 1
                right += 1
            
        return res
