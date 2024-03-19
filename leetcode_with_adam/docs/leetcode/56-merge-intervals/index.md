---
tags:
    - Array
    - Sorting
---

# [56 Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)


## Approach 1 Sorting

$O(nlogn)$ in time, O(n) in space.

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]
        for i in range(1,len(intervals)):
            curr_start,curr_end = intervals[i]
            prev_start,prev_end = res[-1]
            if curr_start <= prev_end:
                candidate = [prev_start,max(prev_end,curr_end)]
                res.pop()
                res.append(candidate)
            else:
                res.append(intervals[i])

        return res
```
