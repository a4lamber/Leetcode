---
tags:
    - Array
    - Matrix
    - Depth-First Search
    - Breadth-First Search
---

# 463 Island Perimeter

最优解就是暴力解.

## Approach 1: Brute Force

!!! note
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(1)

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        observation:
        - determine adjacent nodes to see 
            - out of bounds: +1
            - sea: + 1
            - else: + 0                        
        """
        m,n = len(grid),len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                # adjacent nodes, (i-1,j), (i+1,j),(i,j-1),(i,j+1)
                # left
                if grid[i][j] == 0:
                    continue

                curr = 0
                if j-1 < 0 or (j-1 >= 0 and grid[i][j-1] == 0):
                    curr += 1
                # right
                if j+1 >= n or (j+1 < n and grid[i][j+1] == 0):
                    curr += 1
                # top
                if i-1 < 0 or (i-1 >= 0 and grid[i-1][j] == 0):
                    curr += 1                
                # bottom
                if i + 1 >= m or (i+1 < m and grid[i+1][j] == 0):
                    curr += 1

                res += curr
        return res            
```