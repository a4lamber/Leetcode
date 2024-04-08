---
tags:
    - Array
    - Stack
    - Tree
    - Binary Search Tree
    - Recursion
    - Monotonic Stack
    - Binary Tree
---

# 255 Verify Preorder Sequence in Binary Search Tree



## Approach 1: Recursion

比较intuitive的一个解是，利用BST性质, for every single node `X`

- left subtree of node `X` contains only nodes with values less than `X`
- right subtree of node `X` contains only nodes with values greater than `X`

比如说对于

![](./assets/1.excalidraw.png)


```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        observation:
        - pre-order traversal, 记录第一次访问node的数字
        """
        def dfs(lo,hi):
            nonlocal i
            # base case, reach the end without failing
            if i == len(preorder):
                return True
            
            root = preorder[i]
            if root < lo or root > hi:
                return False
            
            i += 1
            left = dfs(lo,root)
            right = dfs(root, hi)
            
            # 有一个找到了即可
            return left or right
        
        i = 0
        return dfs(-inf,inf)
```