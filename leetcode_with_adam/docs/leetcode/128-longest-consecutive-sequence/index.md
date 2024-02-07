---
tags:
    - Array
    - Hash Table
    - Union Find
---
# [128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

We will talk about three approaches:

- brute force solution $O(n^2)$ in time, $O(n)$ in space
- only look for head of the sequence $O(n)$ in time, $O(n)$ in space
- union find, 也能做到$O(n)$ in time, 但需要a lot more code. 以后再来看看吧.

## Approach 1: Brute Force Solution

This is the first solution came to my mind when i saw it. The outer loop is executed at most n times while the inner loop is executed at most n times. So, the time complexity is O(n^2). The space complexity is O(n) because we are using a set to store the numbers.

Since we have to traverse the `nums`, the only thing left for optimize is the inner while loop. 

If you have a sequence like 
```
nums = [100, 4, 200, 1, 3, 2]
```
For the same sequence `[1, 2, 3 ,4]`, we will check 4 times, which is unnecessary. We only need to check the first number of the sequence, and how do we do that? Please see approach 2.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1st pass: get them into the set()
        # 2nd pass: iterate over nums and create a while loop to check the hashmap
        # O(n) in time, O(n) in space
        count = set(nums)

        best_length = 0
        for num in count:
            curr = num
            curr_length = 0
            while curr in count:                            
                curr_length += 1
                curr += 1
            best_length = max(best_length,curr_length)
        
        return best_length
```


## Approach 2: O(n) in time and space

我们知道我们的目标是找到每一个sequence的头部，那么头部有什么区别呢? 头部的前一个数字不在set里面, 所以我们可以用这个特性来优化我们的算法。

```python
# counting sequence from head
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1st pass: get them into the set()
        # 2nd pass: iterate over nums and create a while loop to check the hashmap
        # O(n) in time, O(n) in space
        count = set(nums)

        best_length = 0
        for num in count:
            if num -1 not in count:
                curr = num
                curr_length = 0
                while curr in count:                            
                    curr_length += 1
                    curr += 1
                best_length = max(best_length,curr_length)
        
        return best_length
```

!!! note Note
    同理，for sequence, 决定尾部可以用尾部的下一个数字不在set里面来判断。但人们更倾向于从头部开始计算，因为left -> right is common in a lot of cultures.


## Approach 3 Union Find

