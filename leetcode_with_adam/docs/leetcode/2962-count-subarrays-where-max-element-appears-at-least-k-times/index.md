---
tags:
    - Array
    - Sliding Window
---

# 2962 Count Subarrays Where Max Element Appears at Least K Times

最优解O(n), O(1)

## Approach 1 Sliding Window

先讲O(n), O(n)的解法, 把这个问题分解。我们把符合条件的所有subarray, 变为

- 找到最短的subarray, 满足以index 0结尾且符合最大值出现次数大于等于k
- 找到最短的subarray, 满足以index 1结尾且符合最大值出现次数大于等于k
- ...
- 找到最短的subarray, 满足以index n-1结尾且符合最大值出现次数大于等于k

我们可以用一个hashmap来记录每个数字出现的次数，然后用sliding window即可.

```python
from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        array_max = max(nums)
        res = 0
        left = 0
        hashmap = defaultdict(int)

        for right,num in enumerate(nums):
            hashmap[num] += 1            
            while hashmap[array_max] >= k and left < right:
                if nums[left] == array_max and hashmap[array_max] == k:
                    break
                hashmap[nums[left]] -= 1
                left += 1

            if hashmap[array_max] >= k:                
                res += left + 1
        return res
```


然后做一下优化，我们发现我们只关心max element的个数，所以我们可以用一个max_counter来记录max element的个数，这样我们就可以用O(1)的空间复杂度来解决这个问题, instead of a hashmap.

```python
from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        array_max = max(nums)
        res = 0
        left = 0
        max_counter = 0

        for right,num in enumerate(nums):
            if num == array_max:
                max_counter += 1
            
            # 找到以right结尾，满足条件的最短subarray
            while max_counter >= k:
                if nums[left] == array_max:
                    if max_counter == k:
                        break
                    else:
                        max_counter -= 1
                left += 1            
            if max_counter >= k:
                res += left + 1
        return res

```