---
tags:
    - Array
    - Two Pointers
    - Binary search
    - Sorting
    - Sliding Window
    - Heap (Priority Queue)
---

# 658 Find K Closest Elements


## Approach 1 Binary Search

Given a sorted integer array, find the k closest elements to x in the array. The result should also be sorted in ascending order.

- `|a - x| < |b - x|`
- `|a - x| == |b - x|` and `a < b`

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left,right = 0,len(arr)-k

        while left < right:
            mid = (left + right)//2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
```

