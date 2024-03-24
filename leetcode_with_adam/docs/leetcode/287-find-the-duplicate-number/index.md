---
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Bit Manipulation
---


# [287 Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2024-03-24)

这题有俩constraint:

- You must not modify the array (assume the array is read only).
- You must use only constant, O(1) extra space.


> Follow up:
> 
>   - How can we prove that at least one duplicate number must exist in nums?
>   - Can you solve the problem without modifying the array nums?


考察two pointers的flyod cycle detection on linked list的思想，但是将数组看成一个linked list，数组的index是node，数组的值是next指针指向的node, similar to [142 Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/).



## Approach 1: Two Pointers

没理解，[echoxiaolee](https://leetcode.com/problems/find-the-duplicate-number/solutions/72846/my-easy-understood-solution-with-o-n-time-and-o-1-space-without-modifying-the-array-with-clear-explanation)的答案.

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
    
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
```

## Approach 2 Binary Search

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate
```