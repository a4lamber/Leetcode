---
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Sorting
---

# [349 Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

## Approach 1 Trivial Hashset

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        
        res = set.intersection(set_1,set_2)
        return res
```

## Approach 2 

