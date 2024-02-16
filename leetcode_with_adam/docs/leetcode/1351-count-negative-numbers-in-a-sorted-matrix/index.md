---
tags:
    - Array
    - Matrix
    - Binary Search
---


# [1351 Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=study-plan-v2&envId=binary-search)


用以下combination时候:

- `while left <= right`
- `left = mid + 1 if nums[mid] >= 0`
- `right = mid - 1 if nums[mid] < 0`

离开while loop后，我们拥有的条件是:

- left = right + 1
- **Case 1:** 数组中有小于0的数，那么left指向的是第一个小于0的数
- **Case 2:** 数组中没有小于0的数，也就是全是正整数。那么left指向的是数组的长度

![](assets/1.excalidraw.png)

```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 4,3,2,-1
        def helper(nums):
            res = 0
            n = len(nums)
            left,right = 0,n-1

            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= 0:
                    # condition not satisfied
                    left = mid + 1
                else:
                    right = mid - 1

            # nums[left] being the either the 1st element that smaller than 0
            # or the array is full of positive numbers and we at the end
            if left == n:
                return 0
            else:
                return n - left
            
        res = 0
        for row in grid:
            res += helper(row)
        return res
```