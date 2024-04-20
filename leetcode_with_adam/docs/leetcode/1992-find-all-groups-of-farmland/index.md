---
tags:
    - Array
    - Depth-First Search
    - Breadth-First Search
    - Matrix
---

# 1992 Find All Groups of Farmland


## Approach 1: BFS

利用BFS的性质，以及farmland是rectangle且不连通的性质，我们可以用BFS来搜索每一个farmland的四个角。我们可以用一个hashset来记录已经访问过的farmland，然后从左到右，从上到下搜索，如果当前farmland没有被访问过，我们就用BFS搜索这个farmland的四个角。最后我们返回所有farmland的四个角。

trick在于，我们需要记录top left corner (r1,c1)和bottom right corner (r2,c2), 其实就是bfs的第一层和最后一层，如下图ripple effect of BFS所示:

![](./assets/1.excalidraw.png)


```python
from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        top left (r1,c1)
        bottom right (r2,c2)
        represents to (r1,c1,r2,c2)
        observation: 
        - hashset to store tuple visited = [(r,c),....]
        - left -> right, top -> down scan
        - BFS搜索的最后一层
        """
        res = []
        rows,cols = len(land),len(land[0])
        visited = set()

        def bfs(i,j):
            corners = [i,j]            
            visited.add((i,j))
            q = deque([(i,j)])
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            
            while q:
                r_0,c_0 = q.popleft()
                # infinitesimal steps
                for dr,dc in directions:
                    r,c = r_0 + dr, c_0 + dc
                    if r >= 0 and r < rows and c >=0 and c < cols and (r,c) not in visited and land[r][c] == 1:
                        visited.add((r,c))
                        q.append((r,c))
            # last node will be bottom right corner
            corners.extend([r_0,c_0])
            return corners

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i,j) not in visited:
                    corners = bfs(i,j)                    
                    res.append(corners)
        return res
```