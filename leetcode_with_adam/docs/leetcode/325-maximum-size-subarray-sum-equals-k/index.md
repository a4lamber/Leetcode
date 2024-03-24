---
tags:
    - Hash Table
    - Array
    - Prefix Sum
---


# [325 Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/)

basic prefix sum questions

## Approach 1 Prefix Sum

two-pass solution,

- initialize a hashmap to store the prefix sum and its index
- first pass to pre-process the prefix sum, only maintain the smallest index of the same prefix sum since we want the maximum size
- second pass to see if there is any `curr_sum - k = target` in the hashmap, if so, update the max length if necessary

```python
from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        every subarray can be represented by the difference
        between two subarray that starts from zero.
        C = A - B  
        x x x x [x x x]
                i.   j
        [x x x] x x x x
         i   j
        1. pre-processing to calculate the prefix sum
            [1,-1,5,-2,3] --> [1,0,5,3,6]
            {
                1:0,
                0:1
                5:2,
                3:3,
                6:4
            }
            if the key already in it, we do nothing since we want 
            the min length for B to get max length
        2. we check every curr_num such that
            curr_sum - prefix_sum = k
            curr_sum - k = prefix_sum = target
            check the target
        """        
        prefix_sum_lookup = defaultdict(int)        
        prefix_sum_lookup[0] = -1

        rolling_sum = 0
        for i,num in enumerate(nums):
            rolling_sum += num
            if rolling_sum not in prefix_sum_lookup:
                prefix_sum_lookup[rolling_sum] = i
        
        curr_sum = 0
        res = 0
        for right,num in enumerate(nums):
            curr_sum += num
            target = curr_sum - k
            if target in prefix_sum_lookup:
                left = prefix_sum_lookup[target]
                res = max(res,right-left)
            
        return res
```

Then you realize that 1st pass and 2nd pass look very similar to each other. And more importantly, the previous prefix_sum the 2nd pass is looking up is the smaller prefix_sum that we have seen so far. Therefore, just like in 1 two-sum that we can do 1 pass, same as here

```python
from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_lookup = defaultdict(int)        
        prefix_sum_lookup[0] = -1

        rolling_sum = 0
        res = 0
        for right,num in enumerate(nums):
            # pre-processing
            rolling_sum += num
            target = rolling_sum - k
            if target in prefix_sum_lookup:
                left = prefix_sum_lookup[target]
                res = max(res,right-left)
            
            if rolling_sum not in prefix_sum_lookup:
                prefix_sum_lookup[rolling_sum] = right
                
            
            
        return res
```


