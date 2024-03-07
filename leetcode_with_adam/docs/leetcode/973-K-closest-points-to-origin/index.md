---
tags:
    - Array
    - Math
    - Divide and Conquer
    - Geometry
    - Sorting
    - Heap (Priority Queue)
    - Quickselect
---

# 973 K Closest Points to Origin


## Approach 1: Heap (Priority Queue)


!!! note
    time complexity: $O(k\log n + n)$, $O(n)$ in space for auxiliary data structure
    

```python
import math
from heapq import heapify,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 最近的k个点;
        # 0. write a helper funcion to calculate the distance from point to (0,0)
        # 1. one-pass scan to calculate the distance, O(n), prob store it as (distance, index)
        # 2. heapify it (O(n))
        # 3. pop the first k
        def get_distance(x,y):
            """return the distance from (x,y) to (0,0)"""
            return (x-0)**2 + (y-0)**2
        
        # O(n)
        distances = [(get_distance(point[0],point[1]),i) for i,point in enumerate(points)]
        # O(n)
        heapify(distances)

        res = []
        # O(k*logn)
        while k > 0:
            _, i = heappop(distances)
            res.append(points[i])
            k -= 1
        
        return res
```