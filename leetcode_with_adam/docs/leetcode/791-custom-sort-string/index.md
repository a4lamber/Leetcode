---
tags:
    - Hash Table
    - String
    - Sorting
---

# [791 Custom Sort String](https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11)



## Approach 1 Hash Table + Heap

- 建立一个`dict`来存储order中的字符的rank, 以及求common characters in both `order`  and `s` string
- one pass scan over the `s` to compute `suffix` and `prefix`. 
    - `suffix` is the characters only in `s` but not in `order`, we don't care about the order of them
    - `prefix` is the characters in `s` and in `order`, we need to make sure they appear in the order of `order`, according to the `dict` we built in the first step. The way to do it is to use a `min heap` to store the rank of the characters in `s` and `order`, and then later pop them out in the order of the rank.
- combine `prefix` and `suffix` to get the result

!!! complexity
    - Time: $O(n\log n)$ when scanning over `s` to build `heap`
    - Space: $O(m + n)$

    where $n$ is the length of `s`, and $m$ is the length of `order`


```python
from collections import defaultdict
from heapq import heapify,heappush,heappop
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # for those char appeared in both order and s, we need to make sure they appear in those order.
        # brute force :
        """
        1. find the common characters in both order and s (thinking hash set)
        2. order those common characters , call it common, first
        3. append (s - common) to it
        """
        # for "cba", rank(c) as 1, rank(a) as len("cba")
        order_map = dict()
        order_set = set()
        for rank, char in enumerate(order):
            order_map[char] = rank
            order_set.add(char)
        
        # find the common chars
        common_chars = order_set.intersection(set(s))

        # two pass
        # 1. to get the char in common char
        # 2. get the char only in s but not in order
        prefix = []
        suffix = []
        heap = []
        for c in s:
            # if in both then
            if c in common_chars and c in order_map:
                rank = order_map[c]
                heappush(heap,(rank,c))
            else:
                suffix.append(c)

        while heap:
            _,curr = heappop(heap)
            prefix.append(curr)
                
        return "".join(prefix+suffix)
```


## Approach 2 Frequency Table and Counting

思路是一样的，但是这次用`Counter`来做，更加简洁, 

- 用`Counter`来统计`s`中每个字符的频率
- one-pass scan the `order`, if the character is in counter, then append it to `prefix` x times, where x is the frequency of the character in `s`, i.e. `counter[c]`
- one-pass scan the `counter`, if the character is not in `order` (use a hashset for faster lookup), then append it to `suffix` x times, where x is the frequency of the character in `s`, i.e. `counter[c]`

!!! Complexity
    - Time: $O(n)$ in building `counter`, O(26) in both linearly scanning `order` and `counter`
    - Space: $O(26)$ for counter, prefix + suffix takes $O(n)$, O(26) for order_set

    where $n$ is the length of `s`.

```python
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        1. Counter(s)
        {
            "a": 2,
            "c": 1,
            "d": 2,
            ...
        }
        2. one-pass to generate prefix for common chars
        3. one-pass to generate prefix for non-common chars
        """
        counter = Counter(s)


        prefix = []
        for c in order:
            if c in counter:
                frequencies = counter[c]
                prefix += [c] * frequencies
        
        suffix = []
        order_set = set(order)
        for c in counter:
            if c not in order_set:
                frequencies = counter[c]
                suffix += [c] * frequencies
        
        return "".join(prefix+suffix)
```

Clean the method up a little bit and write it pythonic

```python
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        1. Counter(s)
        {
            "a": 2,
            "c": 1,
            "d": 2,
            ...
        }
        2. one-pass to generate prefix for common chars
        3. one-pass to generate prefix for non-common chars
        """
        # O(n), n length of s
        counter = Counter(s)
        
        # O(m), m length of order
        prefix = [c * counter[c] for c in order if c in counter]
        
        # O(k), k is the number of unique chars in "s", worst case degenrates to O(n), when char in s is all unique
        order_set = set(order)
        suffix = [c * freq for c,freq in counter.items() if c not in order_set]
        
        return "".join(prefix+suffix)
```