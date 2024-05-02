---
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Sorting
---

# 2441 Largest Positive Integer That Exists With Its Negative

## Approach 1: Sorting + two pointers

```python
from heapq import heapify, heappush,heappop
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        objective:
        - find the largest positive negative pair (1,-1)
        observation:        
        - it doesn't contain zero
        solution 1:
        - maintain a max heap and a min heap, keep popping the 
        the last value until meet be the same, O(n) in time & space.
        solution 2:
        - sort it, then two pointer O(nlogn) O(1)
        """
        nums.sort()

        l,r = 0,len(nums)-1
        found = False
        res = None
        while l < r:
            # not possible case
            if nums[l] >0 or nums[r] < 0:
                break         
            # base case
            if nums[l] == -nums[r]:
                found = True
                res = nums[r]
                break

            # going the absolutely smaller one
            if abs(nums[l]) < abs(nums[r]):
                r -= 1
            else:
                l += 1
        if found:
            return res
        else:
            return -1
```