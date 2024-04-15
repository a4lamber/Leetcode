---
tags:
    - Tree
    - Depth-first Search
    - Binary Tree
---

# 129 Sum Root to Leaf Numbers



## Approach 1 Iterative DFS

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        obvervation:
        - dfs, since it's unable to determine when is the leaf node reached        
        - path to sum系列问题
        
        edge cases:
        - leading zeros at root for example
        """
        res = []        
        curr = root
        stack = [(curr,'')]
        res = 0
        while stack:
            node, root_to_curr = stack.pop()

            root_to_curr += str(node.val)

            if not node.left and not node.right:
                res += int(root_to_curr)
            
            if node.left:
                stack.append((node.left,root_to_curr))
            if node.right:
                stack.append((node.right,root_to_curr))
        return res
```

有几个小优化:

- string costs more space than int, so we can use int to represent the path
- string concatenation is expensive

|-|string|int|
|-|-|-|
|累加|`root_to_curr += str(node.val)`|`curr_val = 10*curr_val + node.val`|



```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        obvervation:
        - dfs, since it's unable to determine when is the leaf node reached        
        - path to sum系列问题
        
        edge cases:
        - leading zeros at root for example
        """
        res = []        
        curr = root
        stack = [(curr,0)]
        res = 0
        while stack:
            node, curr_val = stack.pop()

            curr_val = 10*curr_val + node.val

            if not node.left and not node.right:
                res += curr_val
            
            if node.right:
                stack.append((node.right,curr_val))
            if node.left:
                stack.append((node.left,curr_val))
            
        return res
```