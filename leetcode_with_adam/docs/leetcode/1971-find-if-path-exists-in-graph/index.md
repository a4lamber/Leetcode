---
tags:
    - Depth-First Search
    - Breadth-First Search
    - Graph
    - Union Find
---

# 1971 Find if Path Exists in Graph

graph的入门，是要开始整理graph的题目了.

## Approach 1 DFS

```python
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # DFS recursive implementation
        # 1. convert edge set rep of graph to adjacency List (with hashmap)
        # 2. define an array to mark visited node
        # 3. pre-order DFS 

        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        marked = [False for _ in range(n)]
        stack = [source]

        while stack:
            curr = stack.pop()
            if curr == destination: return True

            if not marked[curr]:
                marked[curr] = True

                for next_node in graph[curr]:
                    if not marked[next_node]:
                        stack.append(next_node)

        return False
```