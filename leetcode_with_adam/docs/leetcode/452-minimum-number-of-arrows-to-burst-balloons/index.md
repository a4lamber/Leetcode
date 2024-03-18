---
tags:
    - Array
    - Greedy
    - Sorting
---

# 452 Minimum Number of Arrows to Burst Balloons

感觉不到greedy, 可能还是不敏感.

## Approach 1 Sorting + Greedy

!!! note "complexity"
    O(nlogn) in time, O(n) in space. Sorting takes O(nlogn) time, and we use O(n) space to store all the intersections

The main intuition is that we can only kill multiple birds with one arrow if they are overlapping. In another words, it exists an intersection $\left[x_{start},x_{end}\right]$ that all the balloons have that in their own range. We just need to maintain a list of intersections and return the length of it. The steps are,

- sort `points` by start location
- iterate through `points` and find the intersection

!!! note "Code Implementation"

    ```python
    class Solution:
        def findMinArrowShots(self, points: List[List[int]]) -> int:
            # 1. sort by start location, now we have an Array with ascending start time
            # 2. trying to find the intersection of it
            # 3. return len(Array)
    
            points.sort(key=lambda x:x[0])

            res = [points[0]]

            for i in range(1,len(points)):
                curr_start,curr_end = points[i]
                prev_start,prev_end = res[-1]
                if curr_start >= prev_start and curr_start <= prev_end:
                    # we have an intersection!
                    candidate = [curr_start, min(prev_end,curr_end)]
                    res.pop()
                    res.append(candidate)
                else:
                    # not meragable
                    res.append(points[i])
            
            return len(res)
    ```

We can make two improvement over the above code,

- we maintained an Array `res` to store the intersection range. But we only care about the last element of it. So we just maintain a variable for the last intersection range and another variable for counting number of errors. The intuition is we already sort it by start time.
- since we sort it by start_time already, we can simplify `curr_start >= prev_start and curr_start <= prev_end` to `curr_start <= prev_end`. No need for redundant check.

!!! note "space optimized"
    ```python
    class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])

        res = points[0]
        arrows = 1
        # actually we don't even care about the anything other than the last element in the Array
        # we might as well just use a plain list instead of list of list.
        for i in range(1,len(points)):
            curr_start,curr_end = points[i]
            prev_start,prev_end = res
            if curr_start <= prev_end:
                # we have an intersection, 一箭双雕
                candidate = [curr_start, min(prev_end,curr_end)]
                res = candidate
            else:
                # not meragable
                res = points[i]
                arrows += 1
        
        return arrows
    ```
