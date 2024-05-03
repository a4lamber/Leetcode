---
tags:
    - Two Pointers
    - String
---

# 165 Compare Version Numbers

## Approach 1: Three pass solution

直接想到的解, `str.split('.')` 然后比较每个数字, linear scan了三次

- version1 scan 1次 costs O(m)
- version2 scan 1次 costs O(n)
- compare 1次 costs O(max(m,n))

!!! note
    
    $O(max(n,m))$ in time, $O(m+n)$ in space


```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = version1.split('.')
        two = version2.split('.')
        
        
        for i in range(max(len(one),len(two))):
            left = 0 if i >= len(one) else int(one[i])
            right = 0 if i >= len(two) else int(two[i])

            if left > right:
                return 1
            
            if left < right:
                return -1
            
        return 0
```
