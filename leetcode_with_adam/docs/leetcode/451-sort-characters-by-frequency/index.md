---
tags:
    - Hash Table
    - String
    - Sorting
    - Bucket Sort
    - Heap (Priority Queue)
    - Counting
---

# [451 Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/description/)

这题比较简单，也是bucket sort思想的一种延伸，这里讲三种解法

- hashmap + sorting, O(nlogn) in time, O(n) in space
- bucket sort, array as auxillary DS, O(n) in time, O(n) in space
- bucket sort, hashmap as auxillary DS, O(n) in time, O(n) in space

## Approach 1 hashmap + sorting by value, O(nlogn) in time, O(n) in space

Steps are:

- hashmap 统计每个字符出现的次数
- sorting by value, 从大到小


!!! tip Tip
    `sorted()` in python 不做in-place sorting, 所以不会改变原来的iterable. 无论原来的iterable是`dict()` or `list()`, 返回的都是一个新的list

```python
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        
        res = []
        for i in sorted(hashmap, key=lambda x: hashmap[x], reverse=True):
            res.append(i*hashmap[i])
            
        return "".join(res)
```


## Approach 2 bucket sort, array as auxillary DS, O(n) in time, O(n) in space

Use of array as the auxillary with index as count, value as a list of occured chars, example are:
```python
s = "tree"
#         0      1       2    3   4
bucket = [[],["t","r"],["e"],[], []]
```
Similar idea,
 
- hashmap with key-value pair as `char:count`
- use bucket sort with array

```python
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        # idea of bucket sort: O(n) in time, O(n) in space.
        # construct a hash with char:count
        char_count_hash = defaultdict(int)

        for c in s:
            char_count_hash[c] += 1
        
        # construct a array with index as count, value as a list of occured chars
        # 0. 1.         2.            3.  4
        # [].[] [char,char,char]     [].  []
        bucket = [[] for _ in range(len(s)+1)]

        for char,count in char_count_hash.items():
            bucket[count].append(char)

        res = []
        for i in range(len(bucket) -1, 0,-1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j] * i)
        
        return "".join(res)
```

## Approach 3 bucket sort, hashmap as auxillary DS, O(n) in time, O(n) in space

This approach is similar to approach 2 but slightly more efficient in terms of space. If you use array for bucket sort, you need to build an array of `len(s)`. However, if you use hashmap, you only need to build a hashmap with key as count appeared in the counter, value as a list of occurred chars. On average case, approach 3 with hashmap is more efficient than approach 2 with array in terms of space. But worst case for space complexity, it's the same as approach 2.

```python
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        # idea of bucket sort: O(n) in time, O(n) in space.
        # construct a hash with char:count
        char_count_hash = defaultdict(int)

        for c in s:
            char_count_hash[c] += 1
        
        # construct a hashmap with count --> [char,char]
        bucket = defaultdict(list)
        for char, count in char_count_hash.items():
            bucket[count].append(char)
        
        # we can traverse the length of the string s,
        res = []
        for count in range(len(s),0,-1):
            for char in bucket[count]:
                res.append(char * count)
                            
        return "".join(res)
```