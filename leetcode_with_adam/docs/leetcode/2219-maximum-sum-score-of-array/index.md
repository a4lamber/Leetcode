---
tags:
    - Array
    - Prefix Sum
---
# 2219 Maximum Sum Score of Array

重点在于Approach 2 one-pass solution, 利用了`max()`是commutative的性质，可以在一次遍历中找到最大值。

## Approach 1: two pass

we can maintain two variables that:

- `prefix_sum`: starts at `nums[0]`, keep adding `nums[i]`.
- `suffix_sum`: starts at `sum(nums)`, keep substracting `nums[i]`

one pass for `sum(nums)`, another pass for traversing the array.

```python
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        """
        [4,3,],[-2,5]
        one pass solution by maintaining prefix_sum and suffix_sum        
        """
        n = len(nums)
        
        prefix,suffix = nums[0],sum(nums)
        res = max(prefix,suffix)
        for i in range(1,n):
            prefix += nums[i]
            suffix -= nums[i-1]
            res = max(res,max(prefix,suffix))
        return res
```

## Approach 2: one pass

At each index, we need to compare two value, for every index `i` in nums, we need to compare a total of n pairs, which is `2n` values in total, and we are trying to find the global maximum among `2n` variables. We can save the cost of `sum(nums)` by this trick.

```python
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = suffix = 0
        res = -inf

        n = len(nums)
        for i in range(n):
            prefix += nums[i]
            suffix += nums[n-i-1]
            res = max(res,prefix,suffix)

        return res
```