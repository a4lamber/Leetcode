---
tags:
    - Matrix
    - Heap (Priority Queue)
    - Shortest Path
    - Graph
    - Array
---

# [3342 Find the minimum time to reach last Room II](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/)



## Approach 1 Min Heap + 3-c trick

Very similar to last question. The only difference is that our cost for entering room are variable cost now, instead of being constant cost of 1. Now, the variable cost is alternating between 1 and 2 like `1,2,1,2,1,2,...`.

A nice trick would be use `3-c` to simulate it.


- Time Complexity $O(mnlogmn)$
- Space $O(mn)$

```python
from heapq import heappush,heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # min heap (time,cost,i,j)
        h = [(0,2,0,0)]
        ROWS,COLS = len(moveTime),len(moveTime[0])
        dp = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        

        while h:
            t,c,x,y = heappop(h)
            # termination condition
            if x == ROWS-1 and y == COLS-1:
                return t
            # BFS 4 directions
            for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
                new_x,new_y = x+dx,y+dy

                if new_x >= ROWS or new_y >=COLS or new_x < 0 or new_y < 0:
                    continue                
                # if reach here, it's within boundary
                # calculate new time
                if t >= moveTime[new_x][new_y]:
                    # we can directly go in
                    new_t = t + (3-c)
                else:
                    # barrier to pass
                    new_t = moveTime[new_x][new_y] + (3-c)

                if new_t < dp[new_x][new_y]:
                    heappush(h,(new_t,3-c,new_x,new_y))
                    dp[new_x][new_y] = new_t
```

## Approach 2 (i,j) for cost

We realize that the variable time cost is dependent on your location in the maze,

- at (0,0), your next cost is 1
- at (0,1) your next cost is 2
- at (0,2) your next cost is 1
- ...
- at (x,y) your next cost is `(x+y)%2 + 1`

So we need to maintain 1 less variable.

```python
from heapq import heappush,heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # min heap (time,cost,i,j)
        h = [(0,0,0)]
        ROWS,COLS = len(moveTime),len(moveTime[0])
        dp = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        

        while h:
            t,x,y = heappop(h)
            # termination condition
            if x == ROWS-1 and y == COLS-1:
                return t
            # BFS 4 directions
            for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
                new_x,new_y = x+dx,y+dy

                if new_x >= ROWS or new_y >=COLS or new_x < 0 or new_y < 0:
                    continue                
                # if reach here, it's within boundary
                # calculate new time
                if t >= moveTime[new_x][new_y]:
                    # we can directly go in
                    new_t = t + (x+y)%2 + 1
                else:
                    # barrier to pass
                    new_t = moveTime[new_x][new_y] + (x+y)%2 + 1

                if new_t < dp[new_x][new_y]:
                    heappush(h,(new_t,new_x,new_y))
                    dp[new_x][new_y] = new_t
```