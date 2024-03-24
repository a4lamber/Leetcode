---
tags:
  - Hash Table
  - String
  - Sliding Window
---

# 3 Longest Substring Without Repeating Characters


## Approach 1: Brute Force

The brute force would be:

- enumerate all substrings, $O(n^2)$
- for each substring, check if it has duplicate, comparing `len(substring) == len(set(substring))`
    - `set(substring)` is O(k) on average, where k is the length of the substring.

It rounds to $O(kn^2)$ and If we look at the constraint of the problem, 

- `0 <= s.length <= 5 * 10^4`

It's too much so we have to find a better solution.

## Approach 2: Sliding Window 
Sliding window problem 有以下几个条件要判断作为framework:

- 选什么Auxillary DS (data structure)做window?
    - sliding windowing, 可以选用`list()`或者`set()`来做这件事情，但是由于我们需要判断一个character是否是duplicate inside a string，如果用list作为sliding window, 要做linear search $O(n)$, 然而hashset 为 $O(1), 所以我们prefer `set()`.
- 什么做window的boundary?
    - maintain `left` and `right` pointer (sliding window可以说是双指针法的variation)
- 最简单的case是什么?怎么implement?
    - simplest case `s = sijgopq` non-repeating character. 也就是你的sliding window的右边界(right) traverse the string, 由于没有遇到过repeating char, left pointer stays at index 0. 每一步都add `s[right]` into the hashset. 同时你比较一下现在window的长度和上一个时步的window长度即可;
- 我加什么条件可以从simplest case扩展到general case.
    - 当遇到repeating char, `while s[right] in hashset`, 可以pop左指针指向的current substring最左边的element, 然后左指针进一位，再继续判定`s[right] in hashset`

!!! note 
    由于你的`hashset`中只有unique char, 你根本不care its index. 你只管pop掉这个left pointer指向的char即可.

### Code Implementation

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window (dynamic) using hashset
        left = 0
        res = 0
        hashset = set()

        for right in range(len(s)):
            # 判断新的char是否在hashset之中, O(1)
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            # 假设这个string没有任何重复的，会这么写
            hashset.add(s[right]) # 加入新的char
            
            # 比较当前sliding window大小和以前的最大长度打擂台
            if right - left + 1 > res:
                res = right - left + 1
        
        return res
```

你也可以维护一个dictionary, 但没有set clean.

```python
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window, same direction,
        maintain a key space
        """
        left = 0
        global_max = 0
        uniques = defaultdict(int)
        for right,char in enumerate(s):
            if char not in uniques:
                uniques[char] += 1
            else:
                # we have to move left pointer here
                uniques[char] += 1
                while left < right and uniques[char] > 1:
                    uniques[s[left]] -= 1
                    if uniques[s[left]] == 0:
                        del uniques[s[left]]
                    left += 1
            # if reach here, everything in window is unique
            global_max = max(global_max,right - left + 1)
        return global_max
```