---
tags:
    - Array
    - Sliding Window
    - Hash Table
---

# 2799 Count Complete Subarrays in an Array

## Approach 1: Sliding Window

维护一个hashmap, 分解子问题:

- 以0为结尾的subarray有多少个
- 以1为结尾的subarray有多少个
- ...
- 以n-1为结尾的subarray有多少个

这个可以转化为:

- 以0结尾的，符合条件的最短subarray, 获得子数组首尾，left and right.
- 以1结尾的，符合条件的最短subarray, 获得子数组首尾，left and right.
- ...
- 以n-1结尾的，符合条件的最短subarray, 获得子数组首尾，left and right.

$\sum$后就是答案.

!!! note "complexity"
    
    - time: $O(n)$
    - space: $O(n)$



```python
from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniques = len(set(nums))
        hashmap = defaultdict(int)
        left = 0
        res = 0
        for right,num in enumerate(nums):
            # update hashmap
            hashmap[num] += 1

            while len(hashmap) == uniques:               
                if hashmap[nums[left]] == 1:
                    # if we delete nums[left], we no longer complete
                    break
                hashmap[nums[left]] -= 1
                left += 1
            
            if len(hashmap) == uniques:
                res += left + 1

        return res
```