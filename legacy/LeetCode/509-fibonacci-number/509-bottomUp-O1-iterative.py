class Solution:
    def fib(self, n: int) -> int:
        # memoization (top down) with O(1) space
        # 每一步只取决于前两步
        
        # edge cases
        if n<= 1: return n

        # n >= 2 cases
        current = 0
        prev = 1
        prevPrev = 0

        for i in range(2,n+1):
            # 前两步之和
            current = prev + prevPrev
            prevPrev = prev
            prev = current
        return current
