---
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Prefix Sum
---

# [930 Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14)

第一直觉是sliding window, 但没想出来.

## Approach 1 Prefix Sum + Hash Table

Hashtable记录prefix sum的次数. 我们需要traverse the array, 求total_sum. 在每一个iteration, 我们都做两件事

- 从0开始的subarray的和 == `target` (也就是the sum we are iterating through)
- 在过去的prefix_sum中，找到满足current prefix_sum - previous prefix_sum == target的次数

!!! info "Prefix Sum解决的问题"
    针对连续n个数的和等于target的问题, 可以使用prefix sum + hash的方法来解. hash key是prefix sum的值, value是出现的次数. 用hash的原因是为了储存previous prefix sum的次数. **所有的subarray的和，都可以由两个subarray的prefix sum相减得到.** 你可以思考一下，是不是所有的subarray都可以由两个以0为起点的subarray相减得到？

思考一下info panel里的问题，顺便看看下图,

![](./assets/1.excalidraw.png)

### Code Implementation

```python
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Problem: contiguous k number summing up to goal
        # BF: running all the subarray from length of 1, 2,..., 5
        # O(n^2) for traversing O(n) for summing, O(n^3) total, TLE for size of 3*10^4
        # looking at something O(nlogn) worst
        
        total_count = 0
        prefix_sum = 0
        freq = defaultdict(int)

        for num in nums:
            prefix_sum += num
            if prefix_sum == goal:
                total_count += 1
            
            # check if there is any existing prefix sum that can be subtracted from the curr prefix sum
            # to get the desired goal
            if prefix_sum - goal in freq:
                total_count += freq[prefix_sum - goal]

            # update map
            freq[prefix_sum] += 1
        
        return total_count
```

## Approach 2 Sliding Window

### Code Implementation

```python
```