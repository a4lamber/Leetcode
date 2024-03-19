---
tags:
    - Prefix Sum
    - Array
    - Hash Table
    - Math
---

# 523. Continuous Subarray Sum

与[974 Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)相似.


## Approach 1: Prefix Sum + Hash Table

### Code Implementation
```python
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        1. min length is 2
        2. sum of subarray is multiple of k 
        <--> sum(j..i) % k == 0
        <--> prefix(i) - prefix(j-1) = sum(j..i)
        hashtable:
        {key:value} pair as 
        key --> prefix_sum%2 
        value: min index that satisfies the condition (min j so longer subarray)
        """
        hashtable = defaultdict(int)
        # initial condition
        # 0%k = 0,
        hashtable[0] = -1
        prefix_sum = 0
        for i,num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum%k
            if target in hashtable:
                if i - hashtable[target] >= 2:
                    return True
            else:
                # haven't seen this prefix_sum % k before
                hashtable[target] = i        
        return False
```