---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The number `n` either converge to 1 or `n` forms a loop as you take the sum of all digits.

# Approach
<!-- Describe your approach to solving the problem. -->
two pointer technique for cycle detection.
- check for corner cases 10,100,1000
- set `slow` and `fast` pointer to be `n` 
- advances `slow` one step, `fast` two steps every iteration until `fast` pointer equals to 1. Jump out of the loop when `fast` pointer met `slow` pointer.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def squSumAllDigits(self,n):
        # return the sum of the squares of all digits in n
        # n: int
        # res: int, sum of the squares of its digits
        res = 0
        for char in str(n):
            res += int(char)**2
        
        return res

    def isHappy(self, n: int) -> bool:
        # Constraints: 1<= n <= 2**31 - 1

        # Corner cases: checking for n = 1,10,100 all those number with 1 following trailing zeros
        if self.squSumAllDigits(n) == 1:
            return True
              
        # two pointer, totorise and hare Solution for cycle detection
        slow = n
        fast = n

        # base case: fast !=1
        # jump out of the loop when two pointer met
        while fast != 1:
            # fast pointer advances two steps
            fast = self.squSumAllDigits(fast)
            fast = self.squSumAllDigits(fast)
            # slow pointer advances by one
            slow = self.squSumAllDigits(slow)

            if fast == slow:
                return False
        
        return True

        


```