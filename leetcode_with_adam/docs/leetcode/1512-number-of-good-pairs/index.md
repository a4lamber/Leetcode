---
tags:
    - Array
    - Hash Table
    - Math
    - Counting
---
# 1512-number-of-good-pairs

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashtable = collections.defaultdict(list)
        res = 0
        for i, num in enumerate(nums):
            res += len(hashtable[num])
            hashtable[num].append(i)
        
        return res
```