---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decide to include (goint left)
            subset.append(nums[i])
            dfs(i+1)

            # decide not to include
            subset.pop()
            dfs(i+1)

        # initiate
        dfs(0)
        return res
```

# Reference

- https://www.youtube.com/watch?v=CUzm-buvH_8&ab_channel=HuaHua
- https://www.youtube.com/watch?v=REOH22Xwdkk&ab_channel=NeetCode
