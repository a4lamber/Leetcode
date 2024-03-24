---
tags:
    - Sliding Window
    - Two Pointers
    - String
    - Hash Table
---

# 3090 Maximum Length Substring With Two Occurrences

> Given a string s, return the maximum length of a 
substring such that it contains at most two occurrences of each character.

很经典的hash table题目了， 

## Approach 1 Sliding Window

sliding window, 并且维护一个hashmap with max size 24 for frequency, 对于每一个iteration, 

- traverse the hashmap to see if there is any character with frequency >= 3, if any, we record them in a `hash set`
- `左指针移动条件`: move the left pointer until the frequency of the character in the hashmap is <= 2. 最简单的方法是通过hash set是否为空来判断是否还需要继续移动左指针.



!!! note "complexity"
    - time: $O(24*n)\approx O(n)$
    - space: $O(1)$

```python
from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # sliding window, 
        """
        move right, until we find once occurance > 2
        """
        global_max = 0
        left = 0
        hashmap = defaultdict(int)
        for right,r_char in enumerate(s):
            hashmap[r_char] += 1
            candidates = set()
            for key,freq in hashmap.items():
                if freq >= 3:
                    candidates.add(key)
            # 
            while candidates and left < right:
                hashmap[s[left]] -= 1
                if s[left] in candidates and hashmap[s[left]] <= 2:
                    candidates.remove(s[left])                    
                left += 1
            
            # if ever reach here, we can see if it matches
            global_max = max(global_max,right - left + 1)
                                    
        return global_max
```

