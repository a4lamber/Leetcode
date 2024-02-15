---
tags:
    - Two Pointers
    - String
---

# 1768 Merge Strings Alternately


## Approach 1 Two Pointers

$O(m+n)$ time complexity, $O(m+n)$ space complexity where $m$ is the length of `word1` and $n$ is the length of `word2`

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,r1 = 0,len(word1)
        l2,r2 = 0,len(word2)

        res = []
        while l1 < r1 or l2 < r2:
            if l1 < r1:
                res.append(word1[l1])
                l1 += 1
            if l2 < r2:
                res.append(word2[l2])
                l2 += 1
        
        return "".join(res)
```