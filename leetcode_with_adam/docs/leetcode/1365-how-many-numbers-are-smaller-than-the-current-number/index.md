---
tags:
    - Array
    - Hash Table
    - Sorting
    - Counting
---
# [1365 How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/)

## Approach 1 Brute Force

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # find how many numbers are strictly smaller than this number
        # brute force would be O(n^2)
        res = []
        n = len(nums)
        for i in range(n):
            temp = 0
            for j in range(n):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    temp += 1            
            res.append(temp)
        
        return res
```

## Approach 2 Sorting + Binary Search

发现答案就在排序后的数组中，所以可以先排序，然后用binary search找到每个数字的index, 稍微快一些$O(n\log n)$

```python
from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # for 8, find the index where 8 need to insert to the right like [1,2,2,3,]
        # [1,2,2,3,8]
        # 8, [1,2,2,3] --> 4
        # 1, 0
        # 2. 1
        
        lookup = sorted(nums)
        res = []
        for num in nums:
            index = bisect_left(lookup,num)
            res.append(index)
        return res
```