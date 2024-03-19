---
tags:
    - Array
    - Binary Search
    - Sliding Window
    - Prefix Sum
---

# 209 Minimum Size Subarray Sum

sliding window + prefix sum (rolling in the deep)题型

> **Follow up:** If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

> **Follow up:** 如果你的array中存在负数，你怎么说?

## Approach 1: Sliding Window

由于全是positive integers array, 所以potentially可以用sliding window来解决问题. 我们循环一个数组，顺便记录一个rolling_sum, 

- 每一步，我们更新一下我们的rolling_sum
- 判定`while prefix_sum >= target`, we move the left pointer to the right so we popping one element out of the window

我们不需要check `whicle prefix_sun >= target and l <= r`, 由于题目的constrains, 

- 1 <= target <= $10^9$
- 1 <= nums.length <= $10^5$
- 1 <= nums[i] <= $10^4$


### Code Implementation
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # positive array so we can sliding window
        # we eat element (moving right) when target not meet,
        # we spit out element (moving left) when target has been met
        # we kept a rolling sum
        
        n = len(nums)
        res = n+1
        prefix_sum = 0
        
        l = 0
        for r,num in enumerate(nums):
            prefix_sum += num
            # 不需要担心左边界超过右边界，由于constrains.
            while prefix_sum >= target:
                # update window size
                res = min(res,r-l+1)

                # we have to pop left till empty
                prefix_sum -= nums[l]
                l += 1
        

        return res if res != n+1 else 0
```

## Approach 2: Binary Search

Link [here](https://leetcode.com/problems/minimum-size-subarray-sum/solutions/3729040/o-n-and-o-n-log-n-solution-in-python).


