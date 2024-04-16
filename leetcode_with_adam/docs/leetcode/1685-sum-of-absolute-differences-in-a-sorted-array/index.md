---
tags:
    - Array
    - Math
    - Prefix Sum
---
# 1685 Sum of Absolute Differences in a Sorted Array

## Approach 1 Math

when we are doing the sum of absolute difference, we need to flip sign if the value is greater than the curr value. For example, for `[2,3,5]`, we have the following pattern and generalization
```
for [2,3,5], total_sum = 2 + 3 + 5 = 10, n = 3
result[0] = (+2 -2 -2) + (-2 +3 + 5) = 4     
result[1] = (+3 +3 -3) + (-2 -3 + 5) = 3
result[2] = (+5 +5 +5) + (-2 -3 -5) = 5
...
result[i] = LHS[i] + RHS[i]
where
LHS[i] = (i+1) * nums[i] + (n-(i+1)) * (-1) * nums[i]
and
RHS[0] = total_sum - 2 * nums[0]
RHS[1] = RHS[0] - 2*nums[1]
RHS[2] = RHS[1] - 2*nums[2]
...
...
```

then we can generalize it to

$$
LHS\left[i\right] = (i+1)*nums\left[i\right] - (n-i-1)*nums\left[i\right] \quad 0 \le i < n
$$

where $n$ is the length of the array `nums`, 

$$
RHS\left[i\right] = \begin{cases}
sum(nums) - 2*nums
\left[i \right] \quad i ==0\\
RHS\left[i-1\right] - 2*nums\left[i \right] \quad 1 \le i < n\\
\end{cases}
$$

so the resultant array would be
```python
[LHS[i] + RHS[i] for i in range(len(nums))]
```


### Code Implementation
```python
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        brute force:
        - run every adjacency pair
        trick:
        for [2,3,5], total_sum = 2 + 3 + 5 = 10, n = 3
        result[0] = (+2 -2 -2) + (-2 +3 + 5) = 4     
        result[1] = (+3 +3 -3) + (-2 -3 + 5) = 3
        result[2] = (+5 +5 +5) + (-2 -3 -5) = 5
        ...
        result[i] = LHS[i] + RHS[i]
        
        LHS[i] = (i+1)*nums[i] + (n-(i+1)) * -1 * nums[i]
        
        RHS[0] = total_sum - 2 * nums[0]
        RHS[1] = RHS[0] - 2 * nums[1]
        RHS[1] = RHS[1] - 2 * nums[2]
        """
        prev_sum = sum(nums)
        n = len(nums)
        res = [None for _ in range(n)]
        for i,num in enumerate(nums):
            lhs = (i+1) * num - (n-i-1) * num
            rhs = prev_sum - 2*num
            res[i] = lhs + rhs
            # update
            prev_sum = rhs
        return res
```