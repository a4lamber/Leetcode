---
tags:
    - Tree
    - String
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---

# 988 Smallest String Starting From Leaf

这题tricky的点在于, 从leaf到root, 而不是root to leaf.

## Approach 1 DFS Recursive

由于是string from leaf to root, 寻找所有的path组成的string, 然后找到最小的string. 有几点需要注意:

- node.val 是0-25的数字, 代表a-z. 用`chr()` and `ord()`来转换
- 每一次string concatenation, 都是prefix

### Code Implementation

```python
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        1. record everything to a list
        2. cash in the results
        observation:
        - probably DFS
        """
        def helper(node,curr):
            if not node:
                return None
            
            curr = chr(ord('a') + node.val) + curr

            if node.left and node.right:
                return min(helper(node.left,curr),helper(node.right,curr))
            if node.left:
                return helper(node.left,curr)
            if node.right:
                return helper(node.right,curr)
            return curr
        
        return helper(root,"")
```

## Approach 2 BFS


要特别注意leaf node时，对于空字符串的处理

### Code Implementation

```python
from collections import deque
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return None
        
        # Add root node to deque along with its value converted to a character
        queue = deque()        
        smallest_string = ""
        queue.append([root, chr(root.val + ord('a'))])
        

        while queue:
            # Pop the leftmost node and its corresponding string from deque
            node, current_string = queue.popleft()
            
            # If current node is a leaf node
            if not node.left and not node.right:
                # Update smallest_string if it's empty or current string is smaller
                smallest_string = min(smallest_string, current_string) if smallest_string else current_string
            
            # If current node has a left child, append it to deque
            if node.left:
                queue.append([node.left, chr(node.left.val + ord('a')) + current_string])
            
            # If current node has a right child, append it to deque
            if node.right:
                queue.append([node.right, chr(node.right.val + ord('a')) + current_string])

        return smallest_string
```