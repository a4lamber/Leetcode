---
tags:
    - Math
    - Dynamic Programming
    - Recursion
    - Memoization
---


# [509 Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)

Recursion + DP入门题

## Approach 1 Recursion (top-down)

```python
class Solution:
    def fib(self, n: int) -> int:
        # base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # recurring cases
        return self.fib(n-1) + self.fib(n-2)
```

## Approach 2 Recursion with Memoization

use class variable

```python
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
```

You could also use instance variable

```python
class Solution:
    def __init__(self):
        self.memo = {}
        
    def fib(self, n: int) -> int:
        # check if in memo
        if n in self.memo:
            return self.memo[n]
        
        # base case
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # n>2
            curr = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = curr
            return curr
```

## Approach 3 Tabulation (iterative bottom-up)

```python
class Solution:
    def fib(self, n: int) -> int:
        # base cases
        if n <= 1:
            return n

        # auxillary DS list 
        cache = [None for _ in range(n+1)]
        cache[0],cache[1] = 0,1

        for i in range(2,n+1): # right hand exclusive
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[n]
```


## Approach 4 Tabulation with Space Optimization

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        prev = 0
        curr = 1
        for i in range(2,n+1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr
```