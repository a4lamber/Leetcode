---
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
---

# [506 Relative Ranks](https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08)

这题两种解法,

- sorting (O(nlogn)). Most intuitive.

## Approach 1 Sorting


!!! note "Time complexity"
    
    - O(nlogn) for sorting
    - O(n) for constructing an array of tuples `[(score, index),(score,index),...]`


```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        start off by creating an array of tuples for (score,index)
            temp = [(10,0),(3,1),(8,2),(9,3),(4,4)]
        remember to sort
            temp.sort(key=lambda x:x[0],reverse=True)
        after sorting, the array will look like this
            temp = [(10,0),(9,3),(8,2),(4,4),(3,1)]
        """
        # empty
        if len(score) == 0:
            return []
        
        n = len(score)
        res = [None for _ in range(n)]

        temp = [(num,i) for i,num in enumerate(score)]
        temp.sort(reverse=True)
        for rank in range(n):            
            idx = temp[rank][1]
            if rank == 0:
                medal = "Gold Medal"
            elif rank == 1:
                medal = "Silver Medal"
            elif rank == 2:
                medal = "Bronze Medal"
            else:
                medal = str(rank+1)
            
            res[idx] = medal
        
        return res
```

## Approach 2 Heap (Priority Queue)

效率没变，需要heappush n次。For an array of tuple, 没办法用built-in heapify来做, 那个只能处理array of `numbers` or `str`.

```python
from heapq import heapify,heappush,heappop
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # empty
        if len(score) == 0:
            return []
        
        heap = []
        # n * log(n)
        for i,num in enumerate(score):
            heappush(heap,(-num,i))
        
        rank = 1
        res = [None] * len(score)
        while heap:
            _ , people_idx = heappop(heap)
            if rank == 1:
                medal = 'Gold Medal'
            elif rank == 2:
                medal = 'Silver Medal'
            elif rank == 3:
                medal = 'Bronze Medal'
            else:
                medal = str(rank)
            res[people_idx] = medal
            rank += 1
        return res
```