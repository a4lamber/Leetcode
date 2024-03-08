---
tags:
    - Array
    - Dynamic Programming
    - Greedy
---
# 55 Jump Game

## Approach 1 Greedy

有一个数组，里面的数字代表了可以跳的最大步数，问是否能够跳到最后一个位置，`nums = [2,3,1,1,4]`, 也就是说:

- index `i`: 表达目前在的位置
- `nums[i]`: 表达这个位置能走的最大步数, 1,2,...,`nums[i]`

以这题做个例子，我们可以画出如下选择图, 图中tuple为 (index, nums[index])的pair,


 

### Code Implementation
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force: try out every combination
        # (0,2) --> 1 step or 2 step
        """(i,nums[i])
                (0,2)
            (1,3)   (2,1)
                    (3,1)
                    (4,4)
        """
        # Or 当前的最优解 = index + it's value

        # base case
        n = len(nums)
        if n == 1:
            return True

        curr = 0

        while curr <= n:
            best = 0
            best_index = curr
            for step in range(1,nums[curr]+1):
                new_curr = curr + step
                if new_curr >= n-1:
                    return True
                if new_curr + nums[new_curr] > best:
                    best = new_curr + nums[new_curr]
                    best_index = new_curr                    
            # if not updating, it means, 
            if best == 0:
                return False

            # move curr pointer by that much
            curr = best_index

        return 10

```
