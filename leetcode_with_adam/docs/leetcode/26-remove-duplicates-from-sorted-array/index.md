---
tags:
    - array
    - two pointers
---
# [26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove in-place
        remain = len(nums)
        left = 1
        prev = nums[0]

        while left < len(nums):
            if prev == nums[left]:
                nums[left-1] = "_"
            
            prev = nums[left]        
            left += 1
            
        while "_" in nums:
            nums.remove("_")

        return remain
```