---
tags:
    - Array
    - Sorting
---

# [2740 Find the value of the partition](https://leetcode.com/problems/find-the-value-of-the-partition/description/)



## Approach 1 Sort


Adjacency minimum.

```python
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        smallest = max(nums)
        for i in range(1,len(nums)):
            diff = abs(nums[i] - nums[i-1])
            smallest = min(smallest,diff)
        
        return smallest
```