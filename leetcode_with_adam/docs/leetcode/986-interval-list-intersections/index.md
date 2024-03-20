---
tags:
    - Array
    - Two Pointers
    - Line Sweep
---

# [986 Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/description/)

几种解法

- line sweep
- two pointers, O(m+n) in time


## Approach 1 Line Sweep

自己想出来的，很拉跨.

```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # each list of intervals is pairwise disjoint and sorted.
        """
        instinct: gotta use the sorted feature otherwise it degenerates to O(nlogn)
        - two pointer
        - fancy trick
        sweep line:
        prev != 2, curr == 2, entering it        
        """
        intervals = []
        
        for start,end in firstList:
            intervals.append((start,1))
            intervals.append((end,-1))
        
        for start,end in secondList:
            intervals.append((start,1))
            intervals.append((end,-1))
        
        intervals.sort()

        prev_time = -1
        prev_cost = -1
        res = []
        curr_cost = 0
        for time,cost in intervals:
            curr_cost += cost
            # for cases like [5,5]
            if prev_cost + curr_cost == 1 and prev_time == time and (not res or time != res[-1][1]):
                res.append([time,time])
            elif prev_cost != 2 and curr_cost == 2:
                res.append([time])
            elif prev_cost == 2 and curr_cost != 2:
                res[-1].append(time)
            
            # update
            prev_time,prev_cost = time,curr_cost     
        return res
```

We can improve on the time complexity and readability by

- using the sorted array of `firstList` and `secondList`
- make the logic more clear

试想一下, firstList and secondList都是sorted by start time, 那么他们的end time自然也是sorted. 这不就是merge 4 sorted array吗？recall merge k sorted array. 有点难度的.

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

## Approach 2 Two Pointers

```python
```
