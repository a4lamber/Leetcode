# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. calculate all the possbile leaf-to-root-path, 
        # 2. check if condition met

        # edge case
        if root is None: return False


        # initialize a stack of tuple carrying (node, sumTillThisNodeSoFar)
        stack = [(root,0)]
        pathSum = 0

        while stack:
            node, pathSum = stack.pop()
            pathSum += node.val

            if node.left is None and node.right is None:
                # reach leafnode, we check whether it's equal to the targetSum or not
                if pathSum == targetSum:
                    return True
            
            if node.left:
                stack.append((node.left,pathSum))
            
            if node.right:
                stack.append((node.right,pathSum))
        
        return False
            

        
