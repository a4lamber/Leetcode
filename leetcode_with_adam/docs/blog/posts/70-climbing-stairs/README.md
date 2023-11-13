---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Readme

## Walkthrough
这一题是dynamic programming的入门题目，现在有n节台阶，你每次只能爬1或者2节，你现在这个state i的可能性，只取决于i-1, i-2, 也就是
$$
dp[i] = dp[i-1] + dp[i-2]
$$

我们来看看前面几步就很方便理解了
```python
dp = [1,2]
```
这个数组`dp`中
- `dp[0]`: 代表着爬n=1 (一节台阶的所有可能性)
- `dp[1]`: 代表着爬n=2 (两节台阶的所有可能性)，也就是你走一步或者两步

按照这个逻辑往下推:
- `dp[2]`: 代表着n=3 (爬三节台阶的所有可能性)，由于你腿短，你只能爬一节或者两节台阶，所以说你这一步i的可能性，是从前一个台阶走一步 + 前两个台阶走两步的所有可能性之和;

.... so on so forth

因此
$$
dp[i] = dp[i-1] + dp[i-2]
$$

从逻辑上来讲, 如果你可以一口气跨3，4，5步，那么你current state information is dependent on previous 3, 4, 5 steps, respectively.



