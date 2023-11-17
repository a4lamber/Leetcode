---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Problem

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example
![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```
output: True
```

# Thought process
Two tree are the same tree if and only if
- same structure
- same value

For symmetric tree, the equivalent conditions are:
- same mirrored structure
- same mirrored

From the template of the BFS, we just need to rearrange the order we insert the node in.
```
       e
     /   \
    a     b
   / \   / \
  b   c  d  e
```


```python
# order to compare same tree
queue.appendleft(a.left)
queue.appendleft(b.left)
queue.appendleft(a.right)
queue.appendleft(b.right)

# order to compare similar tree
queue.appendleft(a.left)
queue.appendleft(b.right)
queue.appendleft(a.right)
queue.appendleft(b.left)
```

> Note: for symmetry, compare the medial side with the lateral side for those into anatomy!

# Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Option 1: convert the problem from symmertric tree
        # to "same" tree by comparing root.left and root.right
        # just need to twist the inserting order
        
 
        p = root.left
        q = root.right

        queue = deque([p,q])

        while queue:
            # pop two nodes
            node_1 = queue.popleft()
            node_2 = queue.popleft()

            if node_1 is None and node_2 is None: continue
            if node_1 is None or node_2 is None: return False
            if node_1.val != node_2.val: return False

            # pass 
            queue.appendleft(node_1.left)
            queue.appendleft(node_2.right)
            queue.appendleft(node_1.right)
            queue.appendleft(node_2.left)
            
            
            
        return True
```