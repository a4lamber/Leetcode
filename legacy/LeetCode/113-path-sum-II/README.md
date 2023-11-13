# Problem

Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


# Algorithm

DFS with a stack of tuple that 
```
# a tuple carries three information
(TreeNode(), list(), int)

# explain
(node, [all the nodes value until this point], currSumTillThisNode)
```

- initial condition: (root, [], 0)
- state transition function:
  - for `list()`, append node.val to ti
  - for `int`, track the current sum in this particular root-to-leaf path; This is tracked for evaluation with targetSum




# Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # sum of the node values in the path
        # tuple design: (node, [list so far])
        # DFS
        # Time: O(n)
        # Space:
        
        if root is None: return []

        stack, res = [(root,[],0)], []

        while stack:
            node,prevSumPath,prevSum = stack.pop()
            # spin up a new list
            currSumPath = prevSumPath.copy()
            # update information in current time step
            currSumPath.append(node.val)
            currSum = prevSum + node.val

            # check if leaf node
            if node.left is None and node.right is None and currSum == targetSum:
                res.append(currSumPath)
                
                                
            # check left
            if node.left:
                stack.append((node.left, currSumPath,currSum))

            # check right
            if node.right:
                stack.append((node.right, currSumPath,currSum))

        return res
        
```