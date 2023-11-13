class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1: return 1
        if n == 2: return 2

        # initilize 2 variable to hold previous two values
        prev = 2
        prevPrev = 1

        for i in range(2,n):
            # update prev then prevPrev
            temp = prev
            prev = prev + prevPrev
            prevPrev = temp

        return prev
