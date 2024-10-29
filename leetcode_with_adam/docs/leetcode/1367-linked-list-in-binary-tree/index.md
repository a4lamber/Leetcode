---
tags:
    - Tree
    - Linked List
    - Binary Tree
    - Depth-First Search
---


# 1367 Linked List in Binary Tree

We have a linked list and a binary tree. We need to see whether exists such a downward path in the linked list such that it matches every value in the given linked list.


Downward path hints us that DFS and we either solve it iteratively or recursively.

We need to accompomlish two things:

- `def _dfs():`DFS check linked list and tree until exhaust either ll or t or dismatch.
- `def _check_path()`: call dfs on every node in the tree

!!! important "Complexity"
    
    - Time Complexity: O(mn)
    - Space complexity: O(m+n)


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        return self._check_path(root,head)
    
    def _check_path(self,node: Optional[TreeNode],head: Optional[ListNode]) -> bool:
        if node is None:
            return False
        if self._dfs(node,head):
            return True
        
        # recursively check left and right subtrees
        return self._check_path(node.left,head) or self._check_path(node.right,head)

    def _dfs(self,node: Optional[TreeNode],head: Optional[ListNode]) -> bool:
        """recursively compare the 
        Break condition:
        1. 先走完linkedlist
        2. 先走完tree
        3. value mismatch
        """
        # we are at the end of the linked list (it's good now)
        if head is None:
            return True
        # reach end of tree but linked list is not empty yet
        if node is None:
            return False
        # 
        if node.val != head.val:
            return False
        
        return self._dfs(node.left,head.next) or self._dfs(node.right,head.next)        
```