# [3110 Score of a String](https://leetcode.com/problems/score-of-a-string/description/)

adjacency pair的问题，也需要利用`ord()`获得character的ordinal value (numerical) of unicode coding. 然后对于alphabet, unicode == ASCII. 或者说ASCII是unicode的子集。

## Approach 1

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(1,n):
            prev,curr = ord(s[i-1]),ord(s[i])
            res += abs(curr - prev)        
        return res
```