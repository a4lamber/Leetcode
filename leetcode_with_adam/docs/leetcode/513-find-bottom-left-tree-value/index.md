---
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---

# 513 Find Bottom Left Tree Value


## Approach 1 BFS

想到的第一个思路，问题求最后一层最左边的值，那么我们就可以用BFS, right to left求解。

!!! tip "BFS order"
    - 从左到右BFS先append left child, 再append right child.
    - 从右到左BFS先append right child, 再append left child.

这题求的是最后一个的值，我们有两种思路:

- 写判断条件，如果是最后一个，就`return res`
- 用integer储存每一个node的value, 反正BFS也是要遍历所有的node，不会有额外的时间复杂度.

我选择了第二种方法.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        
        res = 0
        while queue:
            curr = queue.popleft()
            res = curr.val
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        
        return res
```