# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST + in-order traversal
        stack = []
        res = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # at left most, now we step back by 1
            curr = stack.pop()
            # record the value
            res.append(curr.val)
            # go right by 1 step
            curr = curr.right

        return res[k-1] 

