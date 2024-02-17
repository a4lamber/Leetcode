---
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Sorting
---

# [349 Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

这题直接看[follow-up](#facebook-follow-up).

## Approach 1 Trivial Hashset

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        
        res = set.intersection(set_1,set_2)
        return res
```

## Facebook Follow-up

如果给你的俩array是sorted的，有没有什么O(n) time O(1) space的方法？(不计算output array的空间). 用双指针法, 流程图如下, 

![](assets/1.drawio.png)


```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = []
        
        p1,p2 = 0,0

        while p1 < len(nums1) and p2 < len(nums2):
            curr1,curr2 = nums1[p1],nums2[p2]
            # we find the intersecton, now advances both pointer until nums[x] is different from both nums1 and nums2
            if curr1 == curr2:
                res.append(curr1)
                while p1 < len(nums1) and curr1 == nums1[p1]:
                    p1 += 1
                while p2 < len(nums2) and curr2 == nums2[p2]:
                    p2 += 1
                continue
            
            if curr1 > curr2:
                # 由于是sorted, advance p2直到不同
                while p2 < len(nums2) and nums2[p2] == curr2:
                    p2 += 1
            else:
                # advance p1
                while p1 < len(nums1) and nums1[p1] == curr1:
                    p1 += 1
        return res
```
