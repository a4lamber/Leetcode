---
tags:
    - Prefix Sum
    - Array
---

# [370 Range Addition](https://leetcode.com/problems/range-addition/description/)

利用了segment tree里的lazy propagation的思想. 你不需要立刻更新所有的值，而是在需要的时候再更新.

## Approach 1: Brute Force

```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # brute force:
        # increment everything by inc
        res = [0] * length
        for start,end,inc in updates:
            for i in range(start,end+1):
                res[i] += inc
        
        return res
```

## Approach 2: Prefix Sum

Prefix Sum with auxillary DS as array, + traverse backwards to get the final result. For example,

```
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
```
The intuition is that, we can maintain a `prefix` array to indicate at which index, we need to add the `inc` value. Then we can traverse backwards to get the final result.

![](./assets/prefix_1.excalidraw.png)

We don't need n `prefix` array to maintain. JUST apply superposition to combines states since we only interested in the final result and not caring about the intermediate states.

![](./assets/prefix_2.excalidraw.png)


### Code Implementation

```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:        
        """
        Auxillary DS
        x [x x x] x
           1   3
        """
        helper = [0]*length

        for i,j,inc in updates:
            helper[j] += inc
            if i == 0:
                continue
            else:
                helper[i-1] -= inc
        res = [0] * length
        curr = 0
        for i in range(length-1,-1,-1):
            curr += helper[i]
            res[i] = curr
        return res
```

## Approach 3: Postfix Sum

当你做post-fix sum就需要traverse forward.

```python
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:        
        """
        suffix sum

        Auxillary DS (1,3,2)
        x [x x x] x
        0  1 2 3  4
        0  2.    -2
        """
        suffix_sum = [0]*length

        for i,j,inc in updates:
            suffix_sum[i] += inc
            if j == length-1:
                continue
            else:
                suffix_sum[j+1] -= inc

        res = [0] * length
        curr = 0

        for i in range(length):
            curr += suffix_sum[i]
            res[i] = curr

        return res
```