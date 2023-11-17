class Solution:
    def squSumAllDigits(self,n):
        # n: int
        # res: int, sum of the squares of its digits
        res = 0
        for char in str(n):
            res += int(char)**2
        
        return res
    def isHappy(self, n: int) -> bool:
        # 这一题和
        hashmap = {}

        #
        while n!= 1:
            # if not found
            if n not in hashmap.keys():
                hashmap[n] = 1
            else:
                return False
            # update self
            n = self.squSumAllDigits(n)

        return True

        
