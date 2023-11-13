class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # sliding window approach

        # edge case
        if len(s) < 3:
            return 0
            
        # output
        res = 0
        # declare three variables
        a,b,c = s[0],s[1],s[2]

        # compare within the window, then slide forward by 1
        for i in range(0,len(s)-2):
            # determine whether char in window are mutually different
            if a != b and b!=c and a!=c:
                res += 1
            
            # for the last window, you don't need to slide forward since it's over
            if i+3 != len(s):
                a = b
                b = c
                c = s[i+3]
        
        return res

