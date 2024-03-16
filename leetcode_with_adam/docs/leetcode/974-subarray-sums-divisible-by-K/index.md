---
tags:
    - Array
    - Hash Table
    - Prefix Sum
---


# [974 Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)


## Approach 1: Prefix Sum + Hash Table

这题难点在于，怎么把这一题目的sum divisible by k要求，转化为prefix sum equals to k的已知类型。如果两个prefix sum % k的结果相等，则这俩subarray的差形成的subarray必定能被divisiable by k, 见例子

```
x x x  x  [x  x x x]
      j-1  j      i

sum[j..i] = prefix_sum[i] - prefix_sum[j-1]

prefix_sum[i] % k = a
prefix_sum[j-1] % k = a

then we will have,
(prefix_sum[i] - prefix_sum[j-1]) % k = 0
sum[j..i] % k = 0 符合条件
```

如此可知，我们需要一个hashmap来存储`prefix sum % k` as our key，and frequencies as the value. 还有处理左边界，也就是所有以0为起点的subarray，这些subarray的prefix sum % k = 0, 需要找到一个初始条件, 也就是一个空集的和，自然是0，`0%k == 0` as key, `1` as value since it appears once

```
  ""[x x x]  x x  x x x
  -1     i
```


### Code Implementation

```python
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 假设两个prefix sum的modulus相符，则这俩subarray的差形成的
        # subarray比能被divisiable by k
        hashtable = defaultdict(int)
        # initial condition (key:value) 
        # key empty array, counter once
        hashtable[0] = 1
        prefix = total = 0

        for i,num in enumerate(nums):
            prefix += num
            target = prefix % k
            if target in hashtable:
                total += hashtable[target]
            
            hashtable[target] += 1
        
        return total
```