---
tags:
    - Array
    - Binary Search
---

# [744 Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=study-plan-v2&envId=binary-search)


## Problem Statement

这一题给你一个排序好的数组 like `["a","c","z"]`，和一个target letter, 让你找到数组中第一个大于target的letter. 如果找不到，就返回第一个letter.

## Approach 1 Ugly but works

自己写的，非常struggle with the edge cases, 但是最后还是过了. 我的思路是:

- 先寻找target，
    - 如果找到，再linear search找到第一个大于target的数
    - 如果找不到，直接return first element

!!! warning warning
    我这一题这么struggle且solution deteriorate to Linear solution when i have array with low cardinality (edge case) like `["a","a","a","a"]`的原因是，我predicate定义错了.

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0, len(letters)-1

        while left <= right:
            mid = (left + right)//2
            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] < target:
                left = mid + 1
            else:
                # mid is the target
                while mid < len(letters):
                    if letters[mid] > target:
                        return letters[mid]
                    mid += 1
                
                return letters[0]
                # didn't find it
                if mid == len(letters):
                    return letters[0]
                # we find it!
                return mid
            
            # case: we didn't find it and left > right
            # left = right + 1
            if letters[left] <= target:
                while left < len(letters):
                    if letters[left] > target:
                        return letters[left]
                    left += 1
                return letters[0]
            else:
                return letters[left]
```

## Approach 2 Beautiful AF

这题的搜索条件是:
```
找到第一个大于target的数，而不是找到target
```

那这样的话，我们的updates的条件就不只是letters[left] < target而是letters[left] <= target. 这样的话，我们就可以直接用binary search找到第一个大于target的数.
```python
# 应该是
if letters[mid] <= target:
    left = mid + 1
else:
    right = mid - 1

# instead of 
if letters[mid] < target:
    left = mid + 1
elif letters[mid] == target:
    pass
else:
    right = mid - 1
```

当离开while循环后，我们有以下几个性质

- left + 1 = right
- 如果letters中存在符合letter大于target，
    - `letters[left]` is the first letter greater than target
    - `letters[right]` is the last letter less than target
- 如果letters中不存在符合letter大于target，那么left必然已经搜索到了最后一个letter，也没找到大于target的数. 所以, 
    - `left == len(letters)`
    - `nums[left]` >= target恒成立


```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0,len(letters)-1

        while left <= right:
            mid = (left + right)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # when reaches here, left = right + 1 and left is the first index greater than mid
        if left == len(letters):
            # scan the whole array
            return letters[0]
        else:
            return letters[left]
```


