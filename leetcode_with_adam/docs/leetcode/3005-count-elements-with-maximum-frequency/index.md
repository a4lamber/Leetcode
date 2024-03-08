---
tags:
    - Array
    - Hash Table
    - Counting
---

# 3005 Count Elements with Maximum Frequency

One pass solution比较巧妙

## Approach 1 Bucket Sort

利用bucket sort, 先计算counter, 再按frequency放入bucket, 最后从后往前找到最大的frequency, 然后返回最大的frequency的元素个数 x frequency.

```python
from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # 1. get max frequency
        # 2. count how many has that frequency
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        res = 0
        buckets = [[] for _ in range(len(nums)+1)]
        for element,freq in counter.items():
            buckets[freq].append(element)
        
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                return len(buckets[i]) * i
```

## Approach 2 One-Pass

没有复杂度的提升，但是a lot cleaner with one-pass. 我们要解决的三个问题

1. Counter for storing frequency with auxillary DS like hash table
2. compute max frequency
3. get total frequency = max frequency x number of elements @ max frequency

最intuitive的是三分化(bro splitting)，但我们可以用one-pass (compound movement)来解决这个问题. 解的时候注意这个,

- 当你遇到新的max frequency, 以前的记录no longer matters, just nuke everything and start over.
- 当你遇到相同的max frequency, 你只需要增加total frequency.

```python
from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # one-pass
        # 1. counter in auxillary DS
        # 2. max frequency
        # 3. compute max frequency x number of elements @ max frequency
        counter = defaultdict(int)
        max_freq = 0
        total_freq = 0

        for num in nums:
            # increase counter by 1
            counter[num] += 1
            # check if max frequency still hold
            if counter[num] > max_freq:
                # update_max_freq and reset total frequency
                max_freq = counter[num]
                total_freq = max_freq
            elif counter[num] == max_freq:
                # bump up total frequency
                total_freq += max_freq
        
        return total_freq
```