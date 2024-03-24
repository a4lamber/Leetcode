---
tags:
    - Two Pointers
    - String
---

# [408 Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/description/)


## Approach 1 Two Pointers

Be careful with the edge cases like:

- handling leading zero
- handling when we encounter `number`, we can do it in two ways
    - 1
        - maintain a counter the number of digits in the number
        - we do slicing at the end
    - 2
        - we maintain a list to store all digits in the number
        - we join them at the end


```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        1. 遇到"0"
        2. 遇到数字
        3. 不相同的char
        """
        i = j = 0
        m,n = len(word),len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                # non-empty
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                # both are characters
                return False
        
        return i == m and j == n
```