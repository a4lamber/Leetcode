---
tags:
    - Two Pointers
    - Array
    - Sorting
---
# [977 Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)


## Approach 1 Two Pointers

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo,hi = 0,len(nums)-1
        
        res = []
        while lo <= hi:
            if abs(nums[hi]) > abs(nums[lo]):
                res.append(nums[hi]*nums[hi])
                hi -= 1
            elif abs(nums[hi]) < abs(nums[lo]):
                res.append(nums[lo]*nums[lo])
                lo += 1
            else:
                # lo == hi, 只加一次
                res.append(nums[hi]*nums[hi])
                if lo != hi:
                    # lo != hi，再加一次
                    res.append(nums[hi]*nums[hi])
                
                hi -= 1
                lo += 1

        return res[::-1]
```