---
tags:
    - Array
    - Hash Table
    - Stack
    - Monotonic Stack
---
# 496 Next Greater Element I

## Approach 1 Monotonic Stack 

我的思路如下:

- BFS需要$O(mn^2)$的时间复杂度，where `m` and `n` are the length of `nums1` and `nums2`, respectively.
    - for every element in `nums1`, find where `nums1[i] == num2[j]`, then find the next greater element in `nums2` for `nums2[j]`.

既然这样，这个问题变成了两个子问题:

- `problem 1`: 如何找到next greater/smaller element in an array
- `problem 2`: 如何快速找到`nums1[i] == nums2[j]`的index

For `problem 1`, next greater/smaller element is the expertise for monotonic stack.

- we maintain a monotonic stack with larger value at bottom. Whenever we `pop`, it's the time for record the next greater element for the element we `pop`.

For `problem 2`, 

- We need an auxillary DS to help `nums1` to lookup
    - where `nums1[i] == nums2[j]` can be found or not as fast as possible. 
    - this value `nums[i]` should associate with the next greater element in nums2 if it exists.
- 根据这个需求，我想到了hashmap for O(1) lookup. Also using defaultdict to set missing value to -1.


### Code Implementation

```python
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1000, BF: O(n * m * m)
        # descendingly monotonic stack: larger number at bottom, when poping, we find the index
        # tricky: how to deal with not found
        # dry run: [1],[3],[4],[2]
        # auxillary DS:
        #  - allow quick lookup from nums1
        #. - want to grab the index of next greatest value
        # having a hashmap with default to be -1

        # create a stack (list), create a defaultdict with -1 as default

        # travserse nums2, maintaining the monotonic stack and assign value to hash whenever we have a pop

        hashmap = defaultdict(lambda: -1)
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)

        res = [hashmap[num] for num in nums1]

        return res
```



