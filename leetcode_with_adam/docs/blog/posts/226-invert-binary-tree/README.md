---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Problem
Given the `root` of a binary tree, invert the tree, and return its root.

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)


# Solution

The idea is to do the BFS but instead of regular left to right. We do it from right to left.

![](226.excalidraw.png)


# Code

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None: return None

        inverted_root = TreeNode(val = root.val)
        inverted_queue = deque([inverted_root])

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                inverted_curr = inverted_queue.popleft()

                # right append left, left append right
                if curr.right: 
                    queue.append(curr.right)
                    inverted_curr.left = TreeNode(curr.right.val)
                    inverted_queue.append(inverted_curr.left)

                if curr.left: 
                    queue.append(curr.left)
                    inverted_curr.right = TreeNode(curr.left.val)
                    inverted_queue.append(inverted_curr.right)

        
        return inverted_root
```