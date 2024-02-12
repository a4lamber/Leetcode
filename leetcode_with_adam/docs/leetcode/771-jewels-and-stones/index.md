---
tags:
    - Hash Table
    - String
---
# [771 Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

## O(N) time, O(N) space

Arguably, it's O(1) in space since the lookup set is at most 52 characters (26 alphabets x 2).

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookup = set(jewels)
        res = 0
        for stone in stones:
            res += 1 if stone in lookup else 0
        return res
```