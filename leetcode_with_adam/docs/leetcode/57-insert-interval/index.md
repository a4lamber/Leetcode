---
tags:
    - Array
---

# 57 Insert Interval

区间型题目，需要考虑的是如何合并区间。这道理给的`intervals`已经sort by starting time了, 这道题目的思路是在保持`intervals` 还是sorted的性质下，插入`newInterval`，然后merge. 最优解是O(n)的时间复杂度.


## Approach 1 Sorting

懒得想怎么insert, 直接暴力sort. 然后merge intervals.

!!! note "Time/Space Complexity"
    Time Complexity: O(nlogn), for sorting
    Space Complexity: O(1), not counting the output space.

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # non-overlapping
        # 1. append it then re-sort based on starting (Onlogn) --> switch to insert later O(n)
        # 2. 

        # sort by start time
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            curr_start,curr_end = intervals[i]
            prev_start,prev_end = res[-1]
            if curr_start >= prev_start and curr_start <= prev_end:
                # if mergable
                res.pop()
                candidate = [prev_start,max(prev_end,curr_end)]
                res.append(candidate)
            else:
                res.append([curr_start,curr_end])

        return res
```

## Approach 2 Insert and Merge

Find the insertion point for newInterval, then insert it. The insertion point will be set such that the array is still sorted in terms of start time. Then do a one pass solution to merge the intervals.

!!! note "Time/Space Complexity"
    Time Complexity: O(n)
    Space Complexity: O(1), not counting the output space.

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # non-overlapping
        # 1. append it then re-sort based on starting (Onlogn) --> switch to insert later O(n)
        # 2. merge potential overlapping

        # linear scan and insert newInterval mainthing the monotonic increasing for intervals.
        n = len(intervals)
        i = 0
        while i < n and intervals[i][0] < newInterval[0]: 
            i += 1
        
        # now, i will be where we insert
        intervals.insert(i,newInterval)
            
        # O(n) linear scan
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            curr_start,curr_end = intervals[i]
            prev_start,prev_end = res[-1]
            if curr_start >= prev_start and curr_start <= prev_end:
                # if mergable
                res.pop()
                candidate = [prev_start,max(prev_end,curr_end)]
                res.append(candidate)
            else:
                res.append([curr_start,curr_end])

        return res
```
