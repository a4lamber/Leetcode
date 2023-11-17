---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Problem


给一个integer数组，每一个element代表着house中的强，现在假设你是一个robber, 你需要在不能连续偷两个相邻的houses, 抢劫最多的的情况下。不能连续偷两个相邻的houses的原因是会触发报警系统；


我刚做这题的Intuition是, 抢偶数列和奇数列，可以抢最多的houses, 所以统计意义上也能抢最多的东西, 但这并不绝对。答案是用DP的思想



## Example 1
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

## Example 2
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```


## Code Python

记住DP的重要核心思想:
- 每一步都可能是最后一步
- 你这一步的决定如何，完全取决于你过往的步数 (information in the current time step depends on the prev steps or hisotry steps)


```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize an dp list
        dp = list()

        if len(nums) == 0: 
            return 0
        
        dp.append(nums[0])
        if len(nums) == 1:
            return dp[0]
        
        dp.append(max(nums[0],nums[1]))
        if len(nums) == 2:
            return dp[1]

        
        for i in range(2,len(nums)):
            # robber has two choices:
            # Option1: 偷房子i
            # Option2: 不偷房子i, 因为[i-1]的值更大，而且i+1>= 0, 所以这么偷不会亏
            dp.append(max(dp[i-1], dp[i-2] + nums[i]))
        
        return dp[-1]

```