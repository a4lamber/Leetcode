---
tags:
    - Two Pointers
    - String
    - String Matching
---

# [28 Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

作为一个KMP的引子.

## Approach 1: Brute Force

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m = len(haystack),len(needle)
        i = j = 0
        while i < n and j < m:
            if haystack[i] == needle[j]:
                # matching cases
                i += 1
                j += 1
            else:
                # not matching cases, 由于比了j次，所以先backtack by j, 然后再比较下一个index by increment by 1
                i = i - j + 1
                j = 0
            
        if j == m:
            return i - j
        else:
            return -1
```

## Approach 2: KMP

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_pi(pattern):
            m = len(pattern)
            pi = [0] * m
            for i in range(1,m):
                # assign candidate
                j = pi[i-1]
                
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j-1]
                # 到了这里俩可能，j==0 or pattern[i] == pattern[j]
                if pattern[i] == pattern[j]:
                    pi[i] = j+1
                else:
                    # reach j == 0
                    pi[i] = j
            return pi

        n,m = len(haystack),len(needle)
        pi = get_pi(needle)
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - j + 1
        
        return -1
```