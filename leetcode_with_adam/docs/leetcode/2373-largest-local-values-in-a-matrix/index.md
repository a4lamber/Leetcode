---
tags:
    - Array
    - Matrix
    - Simulation
---

# 2373 Largest Local Values in a Matrix

Maxpooling in [CNN](https://paperswithcode.com/method/max-pooling). Mainly used for downsampling the feature map.

## Approach 1 Simulation

- implement a 3x3 maxpooling function to get the largest local value in a 3 by 3 grid

```python
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        def get_max(x:int,y:int) -> int:
            """
            start_i: x coordinate of top left corner
            start_j: y coordinate of top left corner
            """
            res = 0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    res = max(res,grid[i][j])
            return res

        matrix = [[None for _ in range(n-2)] for _ in range(n-2)]
        # downsampling
        for i in range(n-2):
            for j in range(n-2):
                matrix[i][j] = get_max(i,j)
        
        return matrix
```