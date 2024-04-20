---
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Math
---


# 1248 Count Number of Nice Subarrays


## Approach 1 Prefix Sum

用归化的思想，转移成subarray sum equal to k的问题, 也就是[560 subarray sum equal to k](https://leetcode.com/problems/subarray-sum-equals-k/description/)的问题

```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        - nice if there are k odd numbers on it
        we can convert it to
        [1,1,2,1,1] to [1,1,0,1,1]
        [2,4,6] to [0,0,0]
        it became a problem of subarry sum equal to k
        """
        nums = [1 if num % 2 == 1 else 0 for num in nums]
        
        hashtable = collections.defaultdict(int)
        hashtable[0] = 1

        total = 0
        prefix = 0
        for i,num in enumerate(nums):
            prefix += num
            target = prefix - k
            if target in hashtable:
                total += hashtable[target]
            # add the current prefix frequency by 1            
            hashtable[prefix] += 1

        return total
```