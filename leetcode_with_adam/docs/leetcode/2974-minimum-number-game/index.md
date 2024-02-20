---
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
    - Simulation
---
# 2974 Minimum Number Game

实际上考点是sort the top two numbers.

!!! note Note
    Do you know why building a heap with heapify costs $O(n)$ time but sorting costs $O(nlogn)$ time?


```python
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # n % 2 == 0 and n >= 2
        # 1. use a min heap to store the candidates. Heapify 
        # a list (essentially sorting it) is O(n)??
        # 2. pop till empty, each pop is O(logn) and poping n
        # items, approx to O(n * logn)

        res = []
        heapq.heapify(nums)
        
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            res.append(bob)
            res.append(alice)

        return res     
```