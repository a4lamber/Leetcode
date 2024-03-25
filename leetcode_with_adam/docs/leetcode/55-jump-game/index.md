---
tags:
    - Array
    - Dynamic Programming
    - Greedy
---
# 55 Jump Game

又可以贪心，也可以dp. 

- 贪心的思路更加直观，也更加容易理解, 但怎么证明很难.
- dp的思路，更加严谨，但由于dp也是一种枚举, 同时记忆以前的子问题，所以会有更多的空间复杂度.

## Approach 1 Greedy 

有一个数组，里面的数字代表了可以跳的最大步数，问是否能够跳到最后一个位置，`nums = [2,3,1,1,4]`, 也就是说:

- index `i`: 表达目前在的位置index.
- `nums[i]`: 表达这个位置能走的最大步数, 1,2,...,`nums[i]`

我们每一步的行走，可以看作一个子问题。每一个子问题的最优解，用贪心的策略，就是"最有潜力的那一步", 你可以定义为

- 能到达的最远距离: `step + nums[step]`
- 能走出的最大一步: `(step - i) + nums[step]`

以上这两种都是一样的，而step的选择范围，是要看`nums[i]`, 为`[1,2,...,nums[i]]`.

我们做一下dry run, `nums = [2,3,1,1,4]`,

```
we currently at index 0, we can go max 2 steps. No point go 0 step
- we go 1 step, we can then go max 3 steps. Potential is 4
- we go 2 steps, we can then go max 1 steps. Potential is 3

we greedily choose 1 step, because it has the most potential.
```


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

```

## Approach 2 DP

!!! note "complexity"
    - time: O(n^k) where n is the length of the array and k is 最大值域.
    - space: O(n)


```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        倒着来走一遍，
        dp[i]: 能否从index i 跳到终点index n-1
        初始条件:
        dp[n-1] = 1
        state transition function:

        """
        n = len(nums)
        # initialize 
        dp = [False] * n
        dp[n - 1] = True

        for idx in range(n - 2, -1, -1):
            if nums[idx] == 0:
                # 这一步的数值为0，没法走了
                dp[idx] = False
                continue

            # 当前index能走的最远距离
            reach = idx + nums[idx]
            for jump in range(idx + 1, reach + 1):
                # 没跳出界，或者跳到的这一步(jump)为True.
                # jump --> destination, 而idx --> jump, 那我们就可以到终点from idx
                if jump < len(nums) and dp[jump]:
                    dp[idx] = True
                    break

        return dp[0]
```


## Reference

- [striver approach to this in an interview](https://leetcode.com/problems/jump-game/solutions/2375320/interview-scenario-recursion-memoization-dp-greedy).