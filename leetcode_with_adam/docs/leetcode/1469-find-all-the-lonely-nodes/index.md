---
tags:
    - Tree
    - Depth-first Search
    - Breadth-first Search
    - Binary Tree
---
# 1469 Find All The Lonely Nodes

几种做法:

- iterative pre-order DFS with DFS
- recursive DFS

## Approach 1 Iterative Pre-order DFS

```python
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        """
        observation:
        - lonely node is the only child of its parent node. 
            - if parent has left child node, then it must not have right
            - vice versa
        - 每次进stack的时候，做检查
        """
        stack = []
        curr = root
        res = []
        only_child = False
        while stack or curr:
            while curr:
                stack.append(curr)
                if only_child:
                    res.append(curr.val)
                only_child = not curr.right
                curr = curr.left
            
            # reach None, 这时候curr必然没有left child
            curr = stack.pop()
            only_child = not curr.left
            curr = curr.right
        
        return res
```

## Approach 2 Recursive DFS

转化一下lonely child的条件:

- 有parent node
- 且parent node只有一个child node

所以可以利用exclusive OR来判断

```python
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node,parent):
            nonlocal res
            if parent and (not parent.left)^(not parent.right):
                res.append(node.val)
            if node.left:
                dfs(node.left,node)
            if node.right:
                dfs(node.right,node)
        dfs(root,None)
        return res
```