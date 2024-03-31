---
tags:
    - Sliding Window
    - Array
    - Bit Manipulation
---

# [3097 Shortest Subarray with OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/)


## Approach 1: Sliding Window

Some key observation:

- 我们不断的or operation, 其实和prefix_sum一样，你只会增加或不变，但不会减少, 暗示可能是sliding window
- 当你移除左边界的时候，你要undo这个operation, 这个操作会使得prefix_sum减少或不变

这一点，我们可以判断出，这是一个sliding window的题目. 难点在于，怎么正确移除left pointer. 思路如下:

- look at constrains发现`0 <= nums[i] <= 10^9`
- $log_2(10^9) = 30$ by `math.log(10**9,2)` 所以我们可以用一个32 bits可以cover所有的数字
- 我们只有两个操作, prefix or操作后或者nullify操作. 这两次操作都记录下来, increment or decrement the count of the bit involved in the operation
- 当nullify操作，会导致其中一个bit的count变为0, 这个时候，`nullify nums[left]`才会对结果有影响, 这时候我们toggle bits即可.

### Code Implementation


```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        f[i]: the number of times the ith bit is seen in the prefix
        """
        bits = [0 for _ in range(32)]
        n = len(nums)
        prefix = 0
        left = 0
        res = n + 1
        for right in range(n):
            prefix |= nums[right]
            for b in range(32):
                if nums[right] & (1 << b):
                    bits[b] += 1
                
            while prefix >= k and left <= right:
                res = min(res, right - left + 1)
                # undo the operation
                for b in range(32):
                    if nums[left] & (1 << b) > 0:
                        bits[b] -= 1
                        # 如果正好减没了, nullify这个operation才会对结果有影响
                        if bits[b] == 0:
                            # toggle b-th digits, 这就是nullify operation
                            prefix ^= (1 << b)
                left += 1
        
        return res if res != n+1 else -1
```

## Reference

- Explanation [here](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/solutions/4947374/explained-two-pointer-approach-very-simple) 
    - for understand the logic
- [here](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/solutions/4947412/python3-sliding-window-simple-solution)
    - for code implementation
- [larry's video for fun](https://www.youtube.com/watch?v=Sy0DfIuTT8s&ab_channel=ProgrammingLivewithLarry)

