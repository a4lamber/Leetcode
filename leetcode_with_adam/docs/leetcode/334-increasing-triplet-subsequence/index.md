---
tags:
    - Array
    - Greedy   
---

# [334 Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)


If this question is asking for an increasing subarray of length 3, we can just use a strictly monotonically increasing queue to solve it like this,

```python
from collections import deque
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        是否存在一个长度>=3的strictly monotonically increasing queue,
        only works for subarray.
        """
        queue = deque([])
        for i in range(len(nums)):
            while queue and nums[i] <= queue[-1]:
                queue.pop()
            queue.append(nums[i])
            if len(queue) >= 3:
                return True
        return False
```

however, it's asking for subsquence, which means the elements don't have to be contiguous, so the above solution doesn't work. One example would be 

```
[20,100,10,12,5,13]

deque([20])
deque([20, 100])
deque([10])
deque([10, 12])
deque([5])
deque([5, 13])
```

we will never catch `[10,12,13]` since the `5` will just just pushing out `[10,12]`

## Approach 1

The idea is to keep track of the smallest and second smallest number we have seen so far. If we see a number that is greater than both of them, we return True.

!!! note
    You can think of it as an variant or special case of the LIS problem.

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        sec_smallest = float('inf')
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= sec_smallest:
                sec_smallest = num
            else:
                return True
        return False
```

