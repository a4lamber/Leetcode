---
tags:
    - Array
    - Hash Table
    - String
    - Bit Manipulation
    - Counting
---

# 1684 Count the Number of Consistent Strings


```python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        lookup = set(allowed)
        counter = 0
        for word in words:
            for char in word:
                if char not in lookup:
                    counter -= 1
                    break
        return len(words) + counter
```