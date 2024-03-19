---
tags:
    - Array
    - Sorting
---

# [252 Meeting Rooms](https://leetcode.com/problems/meeting-rooms/description/)

没啥可说的, sort by start time and then linear scan.

## Approach 1

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort by the meeting start time, nlogn
        intervals.sort(key = lambda x: x[0])

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
   
        return True
```