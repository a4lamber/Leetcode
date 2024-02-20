---
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
---
# 1464 Maximum Product of Two Elements in an Array

- sorting
- heap(optimal)
- one pass solution(optimal)
    - tracking for top two biggest numbers


## Approach 1 Sorting 

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums[i] > 0 so no negative, maximum product will be the product of top two elements
        # goal: i != j, and max of (nums[i]-1) * (nums[j]-1). return this value
        
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)     
```


## Approach 2 Heap

hacky way to use min heap as max heap in python

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # build a max heap on top of nums, and heapify it with O(n)
        neg_nums = [-1 * num for num in nums]
        heapq.heapify(neg_nums)

        big = heapq.heappop(neg_nums) + 1
        second_big = heapq.heappop(neg_nums) + 1

        return big * second_big
```

## Approach 3 One Pass

track the encounter of top two biggest numbers with one pass solution.

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums[i] >= 1
        big,second_big = 0,0
        for num in nums:
            if num >= big:
                second_big = big
                big = num
            else:
                second_big = max(second_big,num)
        
        return (big - 1) * (second_big - 1)
```