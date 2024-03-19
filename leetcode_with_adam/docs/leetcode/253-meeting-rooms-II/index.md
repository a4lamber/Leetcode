---
tags:
    - Array
    - Two Pointers
    - Greedy
    - Sorting
    - Heap (Priority Queue)
    - Prefix Sum
    - Line Sweep
---
# [253 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/)

这题是interval扛把子题目,几种主要解法

- line sweep
- heap



## Approach 1 Line Sweep

这题和[数飞机](https://www.lintcode.com/problem/391/?utm_source=%5B%27sc-bky-sz-20dec%27%5D)一摸一样, 属于interval的鼻祖题目。代码思路如下

- 构建一个`rooms`数组，大小是intervals的2倍，每个元素是一个tuple of (time,cost)。time是会议开始or结束的时间。cost是1表示开始，-1表示结束
- sort by time ascendingly, if tie, we sort by cost ascendingly (end meeting first). 这和数飞机那题，飞机降落优先于起飞一样. 先结算结束时间，再结算开始时间，这样有利于无缝衔接(上一个meeting刚开完，直接开下一个，不需要新建一个room)
- 维护一个global extremum，再维护一个accumulative_cost.
- 遍历rooms，更新accumulative，然后更新global extremum if necessary

!!! note "complexity analysis"
    $O(nlogn)$ in time due to sorting and $O(n)$ in space

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # since we only interested in the time when the meeting starts and ends
        # size 2n with [(time,cost),(time,cost),....]
        rooms = []
        for start,end in intervals:
            rooms.append((start,1))
            rooms.append((end,-1))
        
        # pass in a tuple as key, so we first sort by time, if tie, we sort by cost (start meeting first)
        rooms.sort(key = lambda x: (x[0],x[1]))

        res = 0
        count = 0
        for _,cost in rooms:
            count += cost
            res = max(res,count)
        return res
```

## Approach 2 Heap

!!! note "complexity analysis"
    $O(nlogn)$ in time due to sorting + linear x heappush and $O(n)$ in space for storing heap

- sort intervals by start time
- 维护一个min heap, 维护所有会议的结束时间
- 遍历intervals，做出判定
    - 如果当前会议的开始时间大于等于heap的最小值，说明有room available，pop出来。反之, 说明frist available room还没有结束呢，再开一个房.
    - 判定之后，不管怎么样都需要assign一个新的room.
- traverse完intervals, 等于所有的会议请求都处理完了，请求完之后，heap里面的元素个数就是最小的room数量了


!!! note "为什么return len(heap)"
    heap里，我们每一个iteration, 肯定会push一个元素进去，选择性的pop一个元素出来。也就是说heap的大小只会增不会减。所以heap的大小就是最小的room数量了. 两个极限情况是所有会议都不重叠，那么这个heap没有pop一次。

```python
from heapq import heapify,heappush,heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        
        # 维护一个min heap, 里面放着所有会议的结束时间
        rooms = []
        heappush(rooms,intervals[0][1])

        for curr_start,curr_end in intervals[1:]:
            # knock knock, room available?
            if curr_start >= rooms[0]:
                # room available了
                heappop(rooms)
            # assign a new room
            heappush(rooms,curr_end)
        
        return len(rooms)
```