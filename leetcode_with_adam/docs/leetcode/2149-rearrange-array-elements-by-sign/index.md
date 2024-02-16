---
tags:
    - Array
    - Two Pointers
    - Simulation
---
# [2149 Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14)

这题讲两个解法:

- with hash O(n) in space and time
- with two pointers O(n) in time and O(n) in space, 
  - 比approach 1少用一个hash
  - 如果output space不算的话，这个方法是O(1) in space

## Approach 1 Hash $O(n)$ in space and time

```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        hashmap = {"p":[],"n":[]}
        for num in nums:
            if num > 0:
                hashmap["p"].append(num)
            else:
                hashmap["n"].append(num)
        
        res = []
        half_length = int(len(nums)/2)
        for i in range(half_length):
            res.append(hashmap["p"][i])
            res.append(hashmap["n"][i])
        
        return res
```

## Approach 2 two pointers $O(n)$ in time and space

```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]

        posi,nega = 0,1

        for i in range(n):
            if nums[i] > 0:
                res[posi] = nums[i]
                posi += 2
            else:
                res[nega] = nums[i]
                nega += 2
        return res
```