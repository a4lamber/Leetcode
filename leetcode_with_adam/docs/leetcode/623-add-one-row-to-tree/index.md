---
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---


# 623 Add One Row to Tree

这题我第一反应是BFS, AC后发现还有DFS的解法. 

## Approach 1 BFS

Intuition says that it must be **BFS**. The rough logic would be to 

- BFS until the layer before the targeted depth `curr_depth = depth - 1`
- add a new layer below the current layer

However, there are a couple of edge cases:

- if `depth == 1`, insert a new node and make the root node it's left node
- if `depth == max_depth`, we add the new layer below the original leaf node
- otherwise, `curr_depth == depth - 1`

How to add the layer? For example, let's consider add between `node` and `node.left`.

- `node.left` exists, we add a `temp = TreeNode(left = node.left)` that it's left pointer to `node.left` and then we point `node.left = temp` to the new node
- `node.left` doesn't exist, we add a new TreeNode points to nothing.

Similarly for node.right.

### Code Implementation
```python
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # edge case
        if depth == 1:
            new_root = TreeNode(val = val,left = root)
            return new_root

        curr = root
        queue = deque([curr])
        curr_depth = 0
        is_layer_added = False
        while queue and not is_layer_added:
            curr_depth += 1
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                # added layer
                if curr_depth == depth - 1 or curr_depth == depth:            
                    if node.left:
                        temp_left = TreeNode(val = val, left = node.left)                        
                        node.left = temp_left
                    else:
                        temp_left = TreeNode(val = val)                        
                        node.left = temp_left
                    if node.right:
                        temp_right = TreeNode(val = val, right = node.right)
                        node.right = temp_right    
                    else:
                        temp_right = TreeNode(val = val)
                        node.right = temp_right
                    is_layer_added = True   

        return curr
```

## Approach 2 DFS (recursive)


## Approach 3 DFS (iterative)



