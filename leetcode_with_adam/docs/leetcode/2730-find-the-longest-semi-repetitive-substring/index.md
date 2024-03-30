---
tags:
    - String
    - Sliding Window
---

# [2730 Find the Longest Semi-Repetitive Substring](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/)


## Approach 1 Sliding Window

拆分子问题,找到:

- 以index 0为终点的，符合条件的最长substring
- 以index 1为终点的，符合条件的最长substring
- ...
- 以index n-1为终点的，符合条件的最长substring



```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        observation:
            - 维护一个counter, 计算num_of_consectuive_pairs if prev == curr
            - sliding window with two pointers
        思路
        - edge case
        - initialize prev at index 0
        - iterate from index 1 to n-1
            - compare prev with curr
            - while num_of_pairs >= 2
                - move left pointer until it doesn't
        Dry run:
            - index 0
            - index 1
            - index 2 522
            - index 3 5223
            - index 4
                - 52233
                - 2233
                - 233 (found it)
        """
        if len(s) == 1:
            return 1
        
        res = 0
        prev = s[0]
        pairs = 0
        left = 0

        for right,curr in enumerate(s[1:],1):
            if curr == prev:
                pairs += 1
            
            while pairs == 2 and left < right:
                if s[left] == s[left+1]:
                    pairs -= 1                     
                left += 1
            
            res = max(res,right - left + 1)
            prev = curr

        return res
```