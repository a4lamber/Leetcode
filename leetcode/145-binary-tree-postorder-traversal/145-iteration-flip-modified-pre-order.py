# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # modified pre-order: (root, right, left) --flip--> post-order (left, right root) 
        stack = []
        res = []
        curr = root

        while stack or curr:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            
            # go back 1 layer, spit out the result
            curr = stack.pop()
            curr = curr.left

        return res[::-1]
            
            
            


            
                
