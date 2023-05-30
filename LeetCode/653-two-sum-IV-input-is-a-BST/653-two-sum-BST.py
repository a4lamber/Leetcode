# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # two sum变种，tree + dict
        look_up = dict()

        # in order traversal
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # reach left-most
            curr = stack.pop()
            # add to
            conjugate = k - curr.val
            if curr.val in look_up.keys():
                # exists in key
                return True
            else:
                look_up[conjugate] = 1

            curr = curr.right

        return False


