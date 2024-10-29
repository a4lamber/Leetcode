---
tags:
    - Hash Table
    - String
    - Binary Search
    - Design
---

# [981 Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/?envType=company&envId=lyft&favoriteSlug=lyft-thirty-days)


## Intuition

这一题我经历了三种思路, 

|思路|description|result|
|-|-|-|
|dictionary + max heap|-|now working|
|dictionary + linear search in array|-|TLE|
|dictionary + binary search in array|-|works!|

这题考点是

- get(key,timestamp)
- set(key,value,timestamp)

这题难点在于get(key,timestamp), return的是key存在，且在[0,timestamp]的闭区间中最大的time插入的数. 我第一个想到的是用max heap maintain sorted list, 但quickly发现，heap的数据并不是按照heap[0]最大, heap[1]第二大来排序的，也就是我们每次都需要打擂台，找到在[0,timestamp]内最大的点, 也是linear search, 和直接用array效率一样，set()还更慢, 如下图


|思路|set()|get()|
|-|-|-|
|dictionary + max heap|$O(logn)$|$O(n)$|
|dictionary + linear search in array|$O(1)$|$O(n)$|

于是采取了appraoch 1,

## Approach 1 Hashmap + array(linear search) TLE

于是我就去implement了, TLE了.

### Code Implementation

```python
from collections import defaultdict
class TimeMap:
    """
    get(timestamp)
    return the largest value among [-\infty, time_stamp] if any, else null

    I am thinking a sorted structure with hash table. Let's say dictionary 
    + array

    [(timestamp,value),....] like 
    {
        "foo" : [(5,100),(2,50),...]
    }

    It's kinda expensive since get() costs O(n) since we will do
    linear scan in it to find a value that matches. set() is cheap with O(1)
    """
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        """
        search
        """
        if key not in self.store or len(self.store[key]) == 0:
            return ""
        
        # find the largest time that within the range[-inf,timestamp]
        max_time_idx = None
        max_time = float('-inf')        
        for idx,item in enumerate(self.store[key]):
            time,value = item
            if timestamp == time:
                return value
            if timestamp >= time and time > max_time:
                max_time = time
                max_time_idx = idx
        if max_time_idx is not None:
            return self.store[key][max_time_idx][1]
        else:
            return ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```


## Approach 2 Hashmap + binary search


我们需要提升O(n) for get(), 那只能提升到$O(1)$ or $O(logn)$. O(1) for get()又不太可能。Additionally, 又因为我们需要找到，在[0,timestamp]范围内的最大的数. 根据这两个前提条件，想到了binary search, 思路就是自己maintain一个sorted array, 满足

- `set()`: 每次插入的时候做一次binary search
- `get()`: 每次获取的时候也做一次binary search

|思路|set()|get()|
|-|-|-|
|dictionary + max heap|$O(logn)$|$O(n)$|
|dictionary + linear search in array|$O(1)$|$O(n)$|
|dictionary + binary search in array|$O(logn)$|$O(logn)$|

!!! tip
    at work, i will probably use a [sorted container](https://pypi.org/project/sortedcontainers/) module. But it's not built-in python so not useful for interview


### Code Implementation

```python
from collections import defaultdict
class TimeMap:
    """
    O(1) for set and O(n) for get won't work. We probably need to do something else. Like maintain
    """
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # insert it directly if it's empty or not in key-space
        if key not in self.store or len(self.store[key]) == 0:
            self.store[key].append((timestamp,value))
        
        # use binary search to insert O(logn), assuming descending order
        # 找到一个小于timestamp的最大的time (most previous)

        left,right = 0,len(self.store[key])-1        
        while left < right:
            mid = left + (right - left)//2
            if self.store[key][mid][0] > timestamp:
                # move left pointer
                left = mid + 1
            else:
                right = mid
        self.store[key].insert(left,(timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        """
        search
        """
        # "为空" 或者 "小于最小值".
        if key not in self.store or len(self.store[key]) == 0 or timestamp < self.store[key][-1][0]:
            return ""
        
        left,right = 0,len(self.store[key])-1        
        while left < right:
            mid = left + (right - left)//2
            if self.store[key][mid][0] > timestamp:
                # move left pointer
                left = mid + 1
            else:
                right = mid
        
        return self.store[key][left][1]
        
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

to make the code dry, we can convert binary search to a private method, 
```python
from collections import defaultdict
class TimeMap:
    """
    O(1) for set and O(n) for get won't work. We probably need to do something else. Like maintain
    """
    def __init__(self):
        self.store = defaultdict(list)

    def _binary_search_in_store(self,key,timestamp):
        left,right = 0,len(self.store[key])-1        
        while left < right:
            mid = left + (right - left)//2
            if self.store[key][mid][0] > timestamp:
                # move left pointer
                left = mid + 1
            else:
                right = mid
        return left
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # insert it directly if it's empty or not in key-space
        if key not in self.store or len(self.store[key]) == 0:
            self.store[key].append((timestamp,value))
        
        # use binary search to insert O(logn), assuming descending order
        # 找到一个小于timestamp的最大的time (most previous)
        res = self._binary_search_in_store(key,timestamp)
        self.store[key].insert(res,(timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        """
        search
        """
        # "为空" 或者 "小于最小值".
        if key not in self.store or len(self.store[key]) == 0 or timestamp < self.store[key][-1][0]:
            return ""
        # binary search
        res = self._binary_search_in_store(key,timestamp)
        
        return self.store[key][res][1]
        
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

