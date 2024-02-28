---
tags:
    - Tree
    - Depth-First Search
    - Binary Tree
---
# [543 Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=daily-question&envId=2024-02-27)


## Approach 1 DFS recursive

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # left-most node VS right-most node
        # recall in order traversal

        diameter = 0

        def dfs(node):
            # base case
            if not node:
                return 0
            
            nonlocal diameter

            # recursive call to the left and right path
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            # update the diameter
            diameter = max(diameter, left_path + right_path)

            return max(left_path,right_path) + 1
        
        dfs(root)
        return diameter
```