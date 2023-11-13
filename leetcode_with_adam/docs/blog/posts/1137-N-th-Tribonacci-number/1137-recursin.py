# recursion解法超时了;
class Solution:
    def tribonacci(self, n: int) -> int:
        # recursion
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 

        
