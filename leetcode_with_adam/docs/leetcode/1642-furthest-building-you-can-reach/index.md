---
tags:
    - Array
    - Greedy
    - Heap (Priority Queue)
---
# [1642 Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/description/?envType=daily-question&envId=2024-02-17)

## 题目描述

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`. You start your journey from building `0` and move to the next building by possibly using bricks or ladders.

While moving from building `i` to building `i+1` (`0-indexed`),
- If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.
- If the current building's height is **less than** the next building's height, you can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

## Approach 1 Heap


这个问题的重点在于，好刚要用在刀刃上，即在最需要的时候使用ladder，而不是在bricks. 逻辑就是，如果你能把目前遇到的最高的diff, 都用ladder解决，那么剩下的diff就用bricks解决。这样的话，就一定能保证到最远。那么如何求你目前为止遇到的最高的diff呢？这就是heap的作用了。

!!! note note
    python's built-in `heapq` is an implementation of min-heap. If you want to use max-heap, a hacky way, you need to multiply the value by -1. Some common operations are: `heapq.heappush(heap,val)`, `heapq.heappop(heap)` and heapify `heapq.heapify(heap)` that turns a list into a heap.

在你traverse `heights`的时候，只要还有砖头，你都假设先用砖头，如果过了，就把diff放到heap里面。如果砖头不够了，就用ladder，同时把目前为止用过的所有砖头的，用过最多的一次砖头，从heap里弹出来，加回所拥有的砖头之中. 这样就能保证你用的砖头最少，ladder最多.

逻辑flowchart如下, 

![](assets/1.drawio.png)

```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            # 不需要用砖头
            if diff <= 0:
                continue
            
            # 假设用了砖头来爬,and also save the diff we used into a max heap 
            bricks -= diff
            heapq.heappush(heap,-diff)
            
            if bricks < 0:
                if ladders == 0:
                    # 弹尽粮绝
                    return i

                ladders -= 1
                bricks += -heapq.heappop(heap)
        
        # if reach here, we go through them all
        return len(heights)-1
```

