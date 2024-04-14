---
tags:
    - Tree
    - Depth-First Search
    - Breadth-First Search
    - Binary Tree
---


# [404 Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14)

有几个解法:

- iterative DFS
- recursive
- Morris Tree Traversal

## Approach 1 DFS

我的第一直觉是不可能是BFS, 因为无法保证leaf node在同一层. 所以我的思路是iterative implementation of DFS with stack. 难点在于我们如何判断left leaf node. Left leaf node的定义是:

- it's a left child of a parent node.
- it's a leaf node.

left node的等价条件很好判断，但是left child就比较难判断了, 如下表

|statement|等价条件|
|-|-|
|it's a left child of a parent node|?|
|it's a leaf node|`not node.left and not not.right`|

所以我们需要在dfs的时候，记录额外的信息来辅助我们判断. 我们可以用一个tuple来储存当前node和是否是left child. 那我们怎么决定是否是left child呢？我们先判断什么时候不是left child:

- root node is not a left child
- 在dfs traversal顺序是先左后右，每次往左走很多步，**每次往右都是前进一格**.这个条件很关键 

在往左的时候，逻辑是
```python
while curr:
    stack.append(curr)
    curr = curr.left
```

我们发现只要stack中每次append的第一个元素，都不是left child. 那么我们只需要用一个flag来manipulate一下即可.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        observation:
        - can't BFS since leaf node might not be on the same layer
        - left leaf满足左边走到头的条件            
        """
        if not root.left and not root.right:
            return 0

        stack = []
        curr = root
        res = 0
        not_left_child = True
        while stack or curr:
            while curr:
                if not_left_child:
                    stack.append((curr,False))
                    not_left_child = False
                else:
                    stack.append((curr,True))
                curr = curr.left
            # now we reach the left leaf node
            # we go back, record the value and going right
            curr,is_left_child = stack.pop()
            if not curr.right and not curr.left and is_left_child:
                res += curr.val
            curr = curr.right
            not_left_child = True
        return res
```

## Approach 2 Morris Tree Traversal 