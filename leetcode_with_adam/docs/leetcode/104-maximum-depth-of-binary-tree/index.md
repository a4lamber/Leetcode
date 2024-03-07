---
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---


# [104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)


## Approach 1 DFS with Recursion

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_height = 1 + self.maxDepth(root.left)
        right_height = 1 + self.maxDepth(root.right)
        return max(left_height , right_height)
```

## Approach 2 DFS (iteration) + stack


## Approach 3 BFS (iteration) + queue