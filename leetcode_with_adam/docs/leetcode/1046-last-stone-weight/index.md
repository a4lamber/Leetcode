---
tags:
    - Array
    - Heap (Priority Queue)
---

# 1046 Last Stone Weight

## Approach 1 Max Heap

```python
from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(n * nlogn)
        # (n)log(n) + (n-1)log(n-1) + ... + (1)log(1)
        # target characteristics of DS:
        # 1 reduce the cost to maintain the sorted structure
        # 2.fast retrivel for maximum 
        # ---> heap 
        # put in negative number to simulate a max heap

        # 1. negagte the stones and heapify the stones
        # 2. pop the stones, unnegagte them.
        #    2.1 when equal, we do nothing,
        #    2.2 when not equal, get the difference of it and put it back
        # 3. go back to step 1 if it has only one stone left or no stones left

        neg_stones = [-1 * stone for stone in stones]
        heapify(neg_stones)

        while len(neg_stones) > 1:
            first = heappop(neg_stones)
            second = heappop(neg_stones)

            if first != second:
                # we put it back
                new_stone = first - second
                heappush(neg_stones,new_stone)

        if (len(neg_stones)) == 1:
            return -1 * neg_stones[0]
        else:
            return 0
```