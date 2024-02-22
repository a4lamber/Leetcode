---
tags:
    - Array
    - Graph
    - Hash Table
---

## 997 Find the Town Judge

入门的图论题目, 有向图的入度和出度的关系, 重点在于理解judge的定义:

- judge的入度是`N-1`
- judge的出度是`0`

用hashmap来记录每个人的入度和出度, 然后遍历一遍hashmap, 找到符合条件的judge.

## Approach 1:

```python
from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # judge: 
        #   incoming: n-1 (every1 trust except himself)
        #   outgoing: 0
        
        # edge case, just 1 person then that person would be judge
        if n == 1: return 1

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for a,b in trust:
            incoming[b] += 1
            outgoing[a] += 1
        
        # check if there is one key that satisfies the above condition
        for candidate,val in incoming.items():
            if val == n - 1 and outgoing[candidate] == 0:
                return candidate
        
        return -1
```



