# Approach 1 Hashmap Linear Space

Self-explanatory. O(n) in time, O(1) in space since it has at most 26 characters.


```python
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:        
        res = -1
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                res = i
                break
        return res            
```
类似的，你可以用`dict().get()` to be more precise.

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1. hashmap to traverse it once
        # 2. traverse twice to see if it's zero
        res = -1
        hashmap = dict()

        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                res = i
                break

        return res
```