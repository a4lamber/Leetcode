---
tags:
    - String
    - Sliding Window
    - Hash Table
---

# [159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)


## Approach 1 Sliding Window

```python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        global_max = 0
        left = 0
        uniques = defaultdict(int)
        for right,r_char in enumerate(s):            
            uniques[r_char] += 1
            while len(uniques) > 2 and left < right:
                uniques[s[left]] -= 1
                if uniques[s[left]] == 0:
                    del uniques[s[left]]
                left += 1
            # if reach here, it's good
            global_max = max(global_max,right-left+1)
            
        return global_max

```