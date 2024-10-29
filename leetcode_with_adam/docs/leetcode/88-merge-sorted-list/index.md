---
tags:
    - Array
    - Two Pointers
    - Sorting
---

# [88 Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

很不错的一道题，这题tricky的解法是

- 如何利用这两个array已经sorted property
- 如何modify in-place

|Approach|Description|Time Complexity|Space complexity|
|-|-|-|-|
|Brute force|构建一个array, 拿m for nums1 and n from nums2, 然后直接用built-in sort|$O\left(\left(m+n\right)log(m+n)\right)$|$O(m)$|
|Two pointer with auxillary array|-|$O(m+n)$|$O(m)$|
|Two pointer but backwards|-|$O(m+n)$|$O(1)$|


## Approach 1 Brute force

最简单的解法, 

- slicing the first m and n element out of nums1 and nums2, respectively. Then concatenate them together
- sort with built in method
- iterate over the array to assign it to nums1 to make it pseudo-in-place-modification

### Solution

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        dummy = nums1[:m] + nums2[:n]
        dummy.sort()

        for i in range(m+n):
            nums1[i] = dummy[i]
```

## Approach 2 Two Pointer forward + Auxillary Array

Steps

- make a copy out of `nums1[:m]` as `nums1_copy` 
- set up two pointer sitting at the head of `nums1_copy` and `nums2`
- read from `nums1_copy` and `nums2` and writes into `nums1`

!!! note
    Be careful that the pointers need to be in the array. 同时也要注意简化条件，因为数据不是从A数组插入C, 就是从B数据插入C. 所以可以简化`if`条件语句.


### Solution

何时从`nums1_copy`读取数据:

- `nums2`已经走完了, 或者
- `nums1`没走完而且`nums1_copy[i]` < `nums2[j]`


```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        copy data from nums1_copy and nums2 into nums1
        nums1_copy: length of m
        nums2: length of n
        nums1: length of m+n
        """
        nums1_copy = nums1[:m]
        i = j = 0

        for p in range(m+n):
            # writes from nums1_copy
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[p] = nums1_copy[i]
                i += 1
            else:
                nums1[p] = nums2[j]
                j += 1        
```

## Approach 3 Two Pointers backward 

这是最优解, in-place modification of array常用思路，倒着two pointer.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        
        for p in range(m + n - 1,-1,-1):
            if j < 0:
                # nums2 is all gone. No need to modify nums1 anymore
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:                
                nums1[p] = nums2[j]
                j -= 1                
```