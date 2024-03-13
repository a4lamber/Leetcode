---
tags:
    - String
    - Sorting
---

# 2785 Sort Vowels in a String

给一个string, 把其中的元音(包括大小写共10个)字母按照ascending顺序重新排序，其它字母保持在`s`中原来的位置。

## Approach 1 Heap

第一个想到的思路就是

- 创建一个min heap，来维护a tuple of (元音字母,对应index), 同时maintain一个list来记录所有的元音字母的index
- one pass to build the heap and the list
- second pass 
    - 遇到元音字母，从min heap中pop出来，append到结果中
    - 非元音字母，直接append `s[i]`到结果中

### Code Implementation
```python
from heapq import heapify,heappush,heappop
class Solution:
    def sortVowels(self, s: str) -> str:
        # a, e, i, o, u
        # "lEetcOde"
        # (E,1),(e,2),(O,5),(e,7)
        # sort them into
        # (E,1),(0,5),(e,2),(e,7)
        # 1. mark all vowels indexs and non-vowels index into two arrays
        # 2. append them into a heap
        # 3. rebuild it from scratch

        vowel_indexes = set()
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        heap = []
        for i,c in enumerate(s):
            if c in vowels:
                vowel_indexes.add(i)
                heappush(heap,(c,i))
            
        
        res = []
        for i in range(len(s)):
            if i in vowel_indexes:
                vowel,_ = heappop(heap)
                res.append(vowel)
            else:
                res.append(s[i])

        return "".join(res)
```

## Approach 2 Counting/Bucket Sort

和bucket sort一样，当值域的search space比元素域小很多时候，我们可以把元素域n, 转化为值域。这一题就是这样的例子，我们的值域是10个元音字母. 大大简化了搜索空间.

- 创建一个hash table来记录每个元音字母的出现次数 (that's why it's called counting sort)
- one pass to build the hash table
- second pass 
    - 遇到元音字母，从hash table中, 根据sorted 10个vowels中，按顺序找到第一个出现次数大于0的元音字母，append到结果中
    - 非元音字母，直接append `s[i]`到结果中


### Code Implementation

```python
from collections import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        counter = Counter(s)
        sorted_vowels = ['A','E','I','O','U','a','e','i','o','u',]
        
        res = []
        # O(n)
        for i,c in enumerate(s):
            # O(10*10), could use a set(sorted_vowels), but one less variable to maintain
            if c in sorted_vowels:                
                for vowel in sorted_vowels:
                    if counter[vowel] > 0:
                        res.append(vowel)
                        counter[vowel] -= 1
                        break
            else:
                res.append(s[i])
        
        return "".join(res)
```