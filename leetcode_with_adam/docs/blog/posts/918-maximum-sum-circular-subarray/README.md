---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Readme

This is another DP problem and it's a variation of [[54 leetcode maximum subarray]]. Essentially the main takeaway is that, maximum subarry is one of the two possibility:
- **Maximum subarray has no circular component**. Just run kadane's algo and you are good to go
- **Maximum subarray has circular component**. 将整个array剔除minimum subarray之后，剩下的remainder就是circular maximum subarray

![](https://leetcode.com/problems/maximum-sum-circular-subarray/Figures/918/918_Maximum_Sum_Circular_Subarray.png)

> 要注意唯一的一个edge cases when all elements in the array is zero, you just return the largest element in the array (同时也是maximum subarray记录的值).
