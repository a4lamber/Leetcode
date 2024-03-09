---
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
---
# [2540 Minimum Common Value](https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09)

第一思路是hash map, 看到是sorted array, 可以用two pointers或者binary search来做。two pointers比较简单，就先做了two pointers.

## Approach 1 two pointers 1 pass

```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 and nums2 are sorted
        p1 = p2 = 0
        m,n = len(nums1),len(nums2)
        while p1 < m and p2 < n:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        
        return -1
```

## Approach 2 Binary Search


```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def binary_search(target, nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False 
        
        # Binary search should be done on the larger array
        # If nums1 is longer, call getCommon with the arrays swapped
        if len(nums1) > len(nums2): 
            return self.getCommon(nums2, nums1)

        # Search for each element of nums1 in nums2
        # Return the first common element found
        for num in nums1:
            if binary_search(num, nums2):
                return num

        # Return -1 if there are no common elements
        return -1
```