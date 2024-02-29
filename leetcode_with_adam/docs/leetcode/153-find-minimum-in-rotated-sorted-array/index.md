---
tags:
    - Array
    - Binary Search
---

# [153 Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

First thing first, we gotta understand the problem. 

## Definition of Rotated Sorted Array

Rotation is a operation that shift the array to the right by 1, if anything go beyond the capacity of the array, it will be put to the start of the array. Kinda like a wrap-around. Let's take `nums = [1, 2, 3, 4, 5]` for example, 

```
rotate 1 time: [5, 1, 2, 3, 4]
rotate 2 times: [4, 5, 1, 2, 3]
rotate 3 times: [3, 4, 5, 1, 2]
rotate 4 times: [2, 3, 4, 5, 1]
rotate 5 times: [1, 2, 3, 4, 5]
......

```

You can conclude that, 

- rotate `n` times wll go back to original where n is the length of the array
- rotate `x` time, will shift the array to the right by x, if any element go beyond the capacity of the static array, it will be put to the start of the array

## Intuition

This question is asking for the minimum element of the array, which is `min(nums)`, but we need something with $O(\log n)$ which is a typical binary search problem.

Then we look at the constrains we are given to construct our search condition:

- `nums` is a sorted ascending array.
- it has unique elements.
- it is rotated `1` to `n` times. It means it has to rotate.

Where the minimum element would be at? It would be at the index `x` where `nums[x-1] > nums[x] < nums[x+1]`. Sort of a valley. We can use `nums = [1,2,3,4,5]` to make an example,

- rotate `1` time: [5, 1, 2, 3, 4], 5> 1 < 2
- rotate `2` times: [4, 5, 1, 2, 3], 4 > 5 < 1
- rotate `3` times: [3, 4, 5, 1, 2], 3 > 4 < 5
- rotate `4` times: [2, 3, 4, 5, 1], 5 > 1, we sitting at the end of the array
- rotate `5` times: [1, 2, 3, 4, 5], 1 < 2, back to original, sitting at start of the array

We know we gonna have `nums[mid]`, `nums[left]` and `nums[right]`  to construct an inequality as our search condition to update `left` and `right` pointers. It can't be `nums[mid] > nums[mid+1]` since we will be at the risk of `mid + 1 >= n` and it will be out of bound. Then, the inequality we can use is limited to,

Search Condition 1

$$
nums[mid] < nums[right]\quad and\quad nums[mid] >= nums[left]
$$

or Search Condition 2

$$
nums[mid] >= nums[right]\quad and\quad nums[mid] < nums[left]
$$

Since we are looking for the minimum element, i.e. the transition element, it has the characteristic of 
being smaller than both its left and right neighbors. We go for Search Condition 1.

The rest of explanation could be found in the code implementation which is pretty thorough.

## Code Implementation

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # - rotate [1,2,3,...,n] and n == len(nums)
        # - rotate n times wll go back to original
        # - roatate x time, will shift the array to the right by 1, if anything go beyond
        # the capacity of the array, it will be put to the start of the array

        # objective: minimum element of this array. index of the minimum element of the array is the
        # one that rotated x time
        
        # find a value that
        # nums[i-1] < nums[i] < nums[i+1]
        
        n = len(nums)
        left,right = 0,n-1

        # 找转折点的故事
        while left < right:
            mid = (left + right)//2
            # if nums[mid] > nums[mid-1] and nums[mid] < nums[i+1]:
            #     return nums[mid]
            if nums[mid] < nums[right]:
                # nums[mid] ... nums[right] must be sorted, 
                # the transition point won't be in this range (mid,right], it is still
                # possible that mid is the transition point, so we can't be aggressive
                right = mid
            else:
                # nums[mid] >= nums[right]. The transition point must be to the right of mid
                # there are chances that mid == right, so we can be more aggressive
                left = mid + 1
        
        return nums[right]
```