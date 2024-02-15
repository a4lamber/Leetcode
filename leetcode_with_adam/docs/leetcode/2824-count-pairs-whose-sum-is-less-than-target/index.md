---
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

# [2824 Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/)


这题很多人用binary search, 但是我感觉会篡改题意. 要求是find the number of pairs in `nums` such that `(i,j)` where `0<=i<j<n` and `nums[i]+nums[j] < target`. 

如果为了用binary search, 你sort了, (i,j)的index就不对了. 

## Approach 1 Brute Force

!!! note Brute Force
    - time complexity is $O(n^2)$
    - space complexity is $O(1)$

```python
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] < target:
                    res += 1
        return res        
```

## Approach 2 Binary Search

留着给未来的自己.
