---
tags:
    - Sliding Window
    - Hash Table
    - String
---


# 340 Longest Substring With At Most K Distinct Characters


## Approach 1 Sliding Window

```python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        k distinct chars + x overlapping chars
        2 pointers, same direction, 
        right: moves only distinct < k (use a counter for freq)
        left: moves when we have len(counter) > k
        maintain a variable for global maximum
        """
        if k == 0:
            return 0
        
        left  = 0
        counter = defaultdict(int)
        global_max = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            while len(counter) > k and left < right:
                counter[s[left]] -= 1
                # clean it if it's zero
                if counter[s[left]] == 0:
                    del counter[s[left]]

                left += 1
            # if reach here, it must be <= k
            global_max = max(global_max,right - left + 1)
        return global_max        
```