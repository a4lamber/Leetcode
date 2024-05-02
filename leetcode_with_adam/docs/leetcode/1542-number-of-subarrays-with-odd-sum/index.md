---
tags:
    - Array
    - Math
    - Dynamic Programming
    - Prefix Sum
---

# 1524 Number of Sub-arrays With Odd Sum


## Approach 1: Prefix Sum

Thought process is explained in the code comments.

```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        brute force: 
            find every single subarray O(n^2) * summing it O(n) --> O(n^3), O(1)
            with pre-compute: O(n^2) --> O(1)
        10^5 --> O(nlogn) at most but most likely a O(n) O(n) solution
        
        intuition
        - we will use prefix sohow
        - for a subarray [x,y,z,...] for it to have odd sum, we can have
            - 0 odd then sum is even
            - 1 odd then sum is odd
            - 2 odd then sum is even
            ...
        it can be generalized such that if we have even number of odd number, then we not good
        x x x [x x x x]
            j.       i
        one edge case
        [x x x] x x x x
       j.    i
        """
        hashtable = {
            'odd': 0,
            'even':1,
        }
        num_of_odd = 0
        res = 0
        for i in range(len(arr)):
            if arr[i]%2 == 1:
                num_of_odd += 1
                
            if num_of_odd %2 == 1:
                # looking for even
                res += (hashtable['even'] % (10**9 +7))
                hashtable['odd'] += 1
            else:
                # looking for odd
                res += (hashtable['odd'] % (10**9 + 7))
                hashtable['even'] += 1
                
        return res  % (10**9 + 7)
```