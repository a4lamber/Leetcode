---
tags:
    - Array
    - Hash Table
    - Sliding Window
---

# [219 Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/)


## Approach 1: Hash Table

维护一个hashtable, 记录每个数字最后一次出现的位置，如果当前数字已经在hashtable中，且当前位置和上一次出现的位置的距离小于等于k，那么就返回True。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # (key:value) as (value: last_seen_index)
        hashtable = {}
        for i,num in enumerate(nums):            
            if num in hashtable and abs(i - hashtable[num]) <= k:
                return True
            hashtable[num] = i
        return False
```

## Approach 2: 暴力

我一开始想出来的solution, 非常脏. 逻辑是维护一个符合条件的sliding window, size为2k, 然后不断的吃进去right pointer, 吐出来left pointer. One-pass traversal时比较当前`nums[i]`是否在window中出现>=2次.

但这个解法的弊端是:

- window和array的两个边界需要handle. 容易出错

```python
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        小于2k的window之中，有没有相同的数字, 遍历n-k次
        <--  1 -->       
        [1,2,3,1]
        """
        n = len(nums)
        if n == 1:
            return False

        hashtable = defaultdict(int)

        for i in range(min(n,k+1)):
            hashtable[nums[i]] += 1
        
        if hashtable[nums[0]] > 1:
            return True
        
        for i in range(1,n):            
            # left pop, right append
            if i - k >= 0:
                hashtable[nums[i-k]] -= 1
            if i + k < n:
                hashtable[nums[i+k]] += 1
            if hashtable[nums[i]] > 1:
                return True
        return False
```