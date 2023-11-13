class Solution:
    def isGood(self,window):
        # return whether all three chars are different to each other
        sliding_hash = {}
        
        for i in range(3):
            if window[i] not in sliding_hash:
                sliding_hash[window[i]] = 1
            else:
                return False

        return True

    def countGoodSubstrings(self, s: str) -> int:
        
        num_good_sub_s = 0

        for i in range(0,len(s)-2):
            if self.isGood(s[i:i+3]):
                num_good_sub_s += 1

        return num_good_sub_s

