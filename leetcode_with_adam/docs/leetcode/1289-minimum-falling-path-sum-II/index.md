---
tags:
    - Array
    - Matrix
    - Dynamic Programming
---

# [1289 Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/description/?envType=daily-question&envId=2024-04-26)



## Approach 1: bottom-up

This is a constrained problem when you can't fall directly down to the same column. Therefore, the optimal path would be falling the last row's minimum value except for the same column. Brute force it will be O(N^3) time complexity. 

!!! note "Complexity"

    - Time complexity: $O(N^3)$
    - Space complexity: $O(N)$


```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # initialize
        prev = grid[0]

        def helper(i,arr):
            """get min of array except for index i
            """
            res = float('inf')
            for j,item in enumerate(arr):
                if j == i:
                    continue
                res = min(res,item)
            return res

        for i in range(1,n):
            curr = [0 for _ in range(n)]
            for j in range(n):
                curr[j] = grid[i][j] + helper(j,prev)

            prev = curr.copy()
        return min(prev)                
```

## Approach 2 Optimized

我们发现，对于每一行，我们只需要找到最小的两个元素，然后更新下一行的值。这样我们可以将时间复杂度降低到$O(N^2)$。

!!! note "Complexity"

    - Time complexity: $O(N^2)$
    - Space complexity: $O(n)$

### Code Implementation

```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        # initialize
        prev = grid[0]
        curr = [0 for _ in range(n)]

        def helper(arr):
            """get two smallest element of an arr and its index
            it returns like [(smallest,idx),(second_smallest,idx)]
            """
            smallest,smallest_i = float('inf'),None
            sec_smallest,sec_i = float('inf'),None

            for i,val in enumerate(arr):
                if val < smallest:
                    sec_smallest,sec_i = smallest,smallest_i
                    smallest,smallest_i = val,i
                elif val < sec_smallest:
                    sec_smallest,sec_i = val,i
            return [(smallest,smallest_i),(sec_smallest,sec_i)]

        for i in range(1,n):            
            lookup = helper(prev)
            for j in range(n):
                if j != lookup[0][1]:
                    curr[j] = lookup[0][0] + grid[i][j]
                else:
                    curr[j] = lookup[1][0] + grid[i][j]
            prev = curr.copy()
        return min(curr)                
```

这里还可以进行优化，其实我们都不care具体的index，只需要知道最小的两个值即可。因此我们可以上一行最小的两个值即可。

!!! note "Complexity"

    - Time complexity: $O(N^2)$
    - Space complexity: $O(1)$

```python
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        
        def get_two_smallest(arr):
            """get two smallest element of an arr and its index
            it returns like [(smallest,idx),(second_smallest,idx)]
            """
            smallest,smallest_i = float('inf'),None
            sec_smallest,sec_i = float('inf'),None

            for i,val in enumerate(arr):
                if val < smallest:
                    sec_smallest,sec_i = smallest,smallest_i
                    smallest,smallest_i = val,i
                elif val < sec_smallest:
                    sec_smallest,sec_i = val,i
            return [(smallest,smallest_i),(sec_smallest,sec_i)]
        # initialize
        prev = get_two_smallest(grid[0])
        
        for i in range(1,n):            
            smallest,smallest_i = float('inf'),None
            sec_smallest,sec_i = float('inf'),None
            for j in range(n):
                if j != prev[0][1]:
                    candidate = prev[0][0] + grid[i][j]
                else:
                    candidate = prev[1][0] + grid[i][j]
                
                if candidate < smallest:
                    sec_smallest,sec_i = smallest,smallest_i
                    smallest,smallest_i = candidate,j
                elif candidate < sec_smallest:
                    sec_smallest,sec_i = candidate,j

            prev = [(smallest,smallest_i),(sec_smallest,sec_i)]
        return prev[0][0]
```