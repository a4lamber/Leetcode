# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # tree traversal iteration solution都依赖于stack
        stack = []
        curr = root
        res = []

        # it only stops when the right-most leaf node's right children node is None and just pops out
        while stack or curr:
            # keep going left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # not more left to go, 
            # 1. go back one layer
            # 2. append value (2nd time visit the node)
            # 3. visit the right
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res


        