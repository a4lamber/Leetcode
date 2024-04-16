---
tags:
    - Array
    - Binary Search
    - Sliding Window
    - Prefix Sum
---

# [1004 Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/description/)


## Approach 1 Sliding Window

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        observation:
        - binary array of 1s and 0s
        - its >= 0, so we can sliding window
        """
        left = 0
        res = 0 
        num_of_zeros = 0       
        for right,num in enumerate(nums):
            if nums[right] == 0:
                num_of_zeros += 1
            while num_of_zeros > k:
                if nums[left] == 0:
                    num_of_zeros -= 1
                left += 1
            # if reach here, it's all valid answer
            res = max(res, right - left + 1)
        return res
```