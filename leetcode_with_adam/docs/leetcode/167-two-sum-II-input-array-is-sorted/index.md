---
tags:
  - Two Pointers
  - Array
  - Binary Search
---

# [167 Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

这一题下意识的反应，是用binary search做，但实际上用two pointer的方法更加灵活。

## Approach 1 Two Pointers

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # constrains: O(1) in space
        # if curr < target, left++
        # if curr > target, right--
        left,right = 0,len(numbers) - 1
        
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1,right + 1]
            elif curr < target:
                left += 1
            else:
                right -= 1
```