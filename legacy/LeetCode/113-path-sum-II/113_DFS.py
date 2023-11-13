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
        


