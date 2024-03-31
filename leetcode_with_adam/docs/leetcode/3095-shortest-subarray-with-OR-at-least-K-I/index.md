---
tags:
    - Bit Manipulation
---

# 3095 Shortest Subarray with OR at Least K I


## Approach 1 Brute Force

```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        observation:
        - special 
        - shortest
        """        
        n = len(nums)
        res = n+1
        
        for j in range(n):
            for i in range(j+1):
                candidate = 0
                for stuff in nums[i:j+1]:
                    candidate |= stuff
                if candidate >= k:
                    res = min(res,j - i + 1)

        return res if res != n+1 else -1
```