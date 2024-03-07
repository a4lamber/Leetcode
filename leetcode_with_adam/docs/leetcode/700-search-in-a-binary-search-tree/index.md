---
tags:
    - Tree
    - Binary Search Tree
    - Binary Tree
---

# 700 Search in a binary search tree

一共三种解法, 

- recursive solution of DFS
- iterative solution of DFS with stack
- iterative solution of BFS with queue

## Approach 1 Recursion

`base case`: 也就是当我们traverse到了`None`的时候, 直接返回`None`即可. 如果`val`等于`root.val`, 那么直接返回`root`即可, 找到答案了.

`recursive case`: 利用BST的性质, 如果`val`小于`root.val`, 那么我们就去左边找, 如果`val`大于`root.val`, 那么我们就去右边找.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root
            # 用return None也可以, 但这里root就是None, 所以直接返回root即可
            # return None
        
        if val == root.val:
            return root
        
        if val < root.val:
            # go to some place smaller
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
```

## Approach 2 Iterative solution of DFS with stack

这题甚至不需要用stack, 因为只需要一个pointer 看比较value就可以了. 其它涉及到DFS的题目, 一般都需要stack, 因为需要记录走过的路径, 但这题不需要.

### Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        while curr:
            if curr.val == val:
                return curr
            elif curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
    
        return None
```


## Approach 3 Iterative solution of BFS with queue

### Code: 暴力BFS

暴力的Breadth First Search, 不利用binary search tree的性质.

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque([root])
        
        while queue:
            curr = queue.pop()
            if curr.val == val:
                return curr
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
        return None
```

### Code: BFS利用BST性质做pruning

利用BST性质做一些pruning, 

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque([root])
        
        while queue:
            curr = queue.pop()
            if curr.val == val:
                return curr
            
            if curr.val > val and curr.left:
                queue.append(curr.left)
            if curr.val < val and curr.right:
                queue.append(curr.right)
                        
        return None
```