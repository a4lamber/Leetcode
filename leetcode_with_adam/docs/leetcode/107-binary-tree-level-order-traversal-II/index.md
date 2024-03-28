---
tags:
    - Tree
    - Breadth-First Search
    - Binary Tree
---

# [107 Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)


## Approach 1 BFS


solve it as regular BFS then we reverse the output by `res[::-1]` or `res.reverse()`, as illustrated in the figure below


![](./assets/107.excalidraw.png)


# Code

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        top to bottom BFS, then UNO reverse card res[::-1]
        """
        if not root:
            return root

        queue = deque([root])
        levels = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop()
                level.append(curr.val)
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
            levels.append(level)
        return levels[::-1] 
```
