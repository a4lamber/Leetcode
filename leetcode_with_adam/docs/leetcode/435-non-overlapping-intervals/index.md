---
tags:
    - Array
    - Sorting
    - Greedy
---

# 435 Non-overlapping Intervals

Greedy, interval的题目. 几种思路，

- brute force, each position, we can either remove or keep the interval, $O(2^n)$
- greedy, first sort


## Approach 1 Sort by Start Greedy

maintain a list of non-overlapping intervals. 我们求minimum number of intervals you need to remove, 也就是求non-overlapping intervals的最大长度, 所以我们的目标就是**尽可能让这个数组越长越好**.

We sort by start time aescedingly, then by end time aescedingly. We will have
```
|----|
|-------|
       |---|
          |---|   
```

我们的步骤是

- sort by start time aescendingly, then by end time aescendingly
- 维护一个数组, 记录non-overlapping intervals
- 判断是否overlap
    - 如果overlap, 又要进行一次判定，是remove新来的curr interval,还是prev interval. 要选择最小的end time的那个interval. 因为end time越大，越有可能overlap with other intervals.
    - 如果不overlap, 就append到res里面

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        
        intervals.sort()

        n = len(intervals)
        # store non-overlapping interval
        res = [intervals[0]]

        # remove larger fish
        for curr_start,curr_end in intervals[1:]:
            prev_start,prev_end = res[-1]

            if curr_start < prev_end:
                # we have overlap! we can remove either 1, but we want to remove the one that's larger and longer
                
                # since the longer the interval, the more likely it's going to over lap with another
                if curr_end >= prev_end:
                    # we remove the curr one
                    continue
                else:
                    # we replace the last one
                    res.pop()
                    res.append([curr_start,curr_end])
                    continue

            res.append([curr_start,curr_end])
        print(intervals)
        return n - len(res)
```


进行下优化，
- 我们只关心last interval的min. 不需要维护整个数组，维护俩变量，一个是non-overlapping interval的数量，一个是`prev_end`用于做判定
- `prev_end`更新如下
    - 如果overlap, 取min
    - 如果不overlap, 直接更新为curr_end

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. start aesc, end aesc
        |----|
            |---|
            |------|
        """        
        
        # store non-overlapping interval
        intervals.sort()

        n = len(intervals)
        _, prev_end = intervals[0]
        num_of_non_overlap = 1

        # remove larger fish
        for curr_start,curr_end in intervals[1:]:
            if curr_start < prev_end:
                # we overlap
                prev_end = min(prev_end,curr_end)
            else:
                # we don't overlap
                prev_end = curr_end
                num_of_non_overlap += 1
                
        return n - num_of_non_overlap
```