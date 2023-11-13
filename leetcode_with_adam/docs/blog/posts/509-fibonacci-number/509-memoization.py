class Solution:
    # class variable, use memoization to store results of previous sub problems
    cache = {0:0,1:1}

    def fib(self, n: int) -> int:
        # bases cases: results in the cache
        if n in self.cache:
            return self.cache[n]

        # update cache
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.cache[n]
