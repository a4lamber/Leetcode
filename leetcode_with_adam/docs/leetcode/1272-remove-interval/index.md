---
tags:
    - Array
---

# [1272 Remove Interval](https://leetcode.com/problems/remove-interval/description/)

Interval三兄弟的老三. 关键是各种边界烦死我了. 我一开始的思路是分类讨论，但被各种边界搞得头大。如下solid line for intervals, dashed line for toBeRemoved interval. 

```
case 1 partial removal (left)
--
 ----
case 2 partial removal (right)
   --
----
case 3 total removal;
 --
----
case 4 cut you in half!
-------
   --
case 5 nothing happens
----
        --
or 
    ----
--
```

实际上可以再整理一下所有的这些可能性，如下表

|case_#|overlap?|append left?|append right?|
|-|-|-|-|
|1|✅ |✅|❌|
|2|✅ |❌|✅|
|3|✅ |❌|❌|
|4|✅ |✅|✅|
|5|❌|N/A|N/A|

!!! tip
    append left, append right代表着你interval被切割之后，是否还剩下左边(靠近start)和右边(靠近end)的部分。如果任意部分有，就以先左后右的顺序append到res里面。

判定逻辑是,

- 先判断是否有overlap
    - 无overlap, 直接append
    - 有overlap, 再判断是否有左右overlap, 有两个if语句描述四种可能性
        - 有左overlap, append left
        - 有右overlap, append right
        - 有左右overlap, append left and right
        - 无左右overlap, append nothing


## Approach 1

```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        remove_start,remove_end = toBeRemoved

        for start,end in intervals:
            # no overlaps at all
            if start >= remove_end or end <= remove_start:
                res.append([start,end])
            else:
                # keep left? strictly less than
                if start < remove_start:
                    res.append([start,remove_start])
                # keep right? strictly greater than
                if end > remove_end:
                    res.append([remove_end,end])
        
        return res
```