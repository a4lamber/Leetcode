---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# 错误算法

由于惯性思维, binary search需要sorted array, 所以我construct了一个array, 这样的话复杂度为
- time complexity: $O(n) + O(logn) \approx O(n)$ 需要declare array那一步的时间复杂度为$O(n)$ 反而比binary search算法本身要慢了, 这里完全可以利用index = value这一特性;

错误算法的代码如下, 

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # create a list of potential Solution
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        # now i need to find soluton within the sorted array
        left = 0
        right = len(nums) - 1

        while left <= right:
            # get mid index of the search space
            mid = (left+right)//2
            # 
            if guess(nums[mid]) == 0:
                return nums[mid]
            elif guess(nums[mid]) == -1:
                right = mid - 1
            else:
                left = mid +1
            

```


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
由于我们需要找的空间为`[1,n]`, 我们不需要构建一个sorted array因为:
- index is already equal to its value
- `[1,n]` is already sorted


# Approach
<!-- Describe your approach to solving the problem. -->

typical binary search算法

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 0
        right = n

        while left <= right:
            # get mid index of the search space
            mid = (left+right)//2
            # 
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid +1
            

```