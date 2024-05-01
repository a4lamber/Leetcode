---
tags:
    - Two Pointers
    - String
---

# 2000 Reverse Prefix of Word



## Approach 1 brute force

```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        1. traverse the string until we found another word[i] == c
        if found, we reverse it
        
        if not found, we just join them together
        """
        N = len(word)
        prefix = []
        found = False
        for i in range(N):
            if word[i] == ch:
                found = True
                prefix.append(word[i])
                break
            prefix.append(word[i])

        if found:
            return ''.join(prefix)[::-1] + word[i+1:]
        else:
            return word
```