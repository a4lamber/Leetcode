---
tags:
    - Math
    - Dynamic Programming
    - Memoization
---

# [1137 N-th Tribonacci number](https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-04-24)

## Approach 1 DP bottom-up


current state information is dependent on the previous 3 states. 

!!! note "Complexity"
    * Time complexity : $O(n)$
    * Space complexity : $O(1)$



### Code Implementation

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        prevprev,prev,curr = 0,1,1

        for _ in range(2,n):
            temp = prevprev + prev + curr            
            curr,prev,prevprev = temp,curr,prev
        
        return curr
```

## Approach 2 Memoization

```python
class Solution:
    # initialize the lookup table
    cache = {0:0,1:1,2:1}
    
    def tribonacci(self, n: int) -> int:
        # base case
        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        return self.cache[n]
```