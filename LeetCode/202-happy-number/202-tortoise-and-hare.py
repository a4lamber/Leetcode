class Solution:
    def squSumAllDigits(self,n):
        # n: int
        # res: int, sum of the squares of its digits
        res = 0
        for char in str(n):
            res += int(char)**2
        
        return res
    def isHappy(self, n: int) -> bool:
        # Constraints: 1<= n <= 2**31 - 1

        # Corner cases: input n 等于10,100,1000这些有且仅有一个1的数字
        if self.squSumAllDigits(n) == 1:
            return True
              
        # two pointer, totorise and hare Solution for cycle detection
        slow = n
        fast = n

        # base case: fast不等于1
        # 当在中间过程中fast = slow at some point, 则跳出，说明cycle
        while fast != 1:
            # fast pointer advances two steps
            fast = self.squSumAllDigits(fast)
            fast = self.squSumAllDigits(fast)
            # slow pointer advances by one
            slow = self.squSumAllDigits(slow)

            if fast == slow:
                return False
        
        return True

        
