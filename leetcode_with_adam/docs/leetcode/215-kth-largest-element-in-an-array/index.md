---
tags:
    - Array
    - Divide and Conquer
    - Sorting
    - Heap (Priority Queue)
    - Quickselect
---

# 215 Kth Largest Element in an Array

## Approach 1 Max Heap

```python
from heapq import heappop,heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-num for num in nums]
        heapify(neg_nums)

        while k > 0:
            curr = heappop(neg_nums)
            k -= 1

        return -curr
```