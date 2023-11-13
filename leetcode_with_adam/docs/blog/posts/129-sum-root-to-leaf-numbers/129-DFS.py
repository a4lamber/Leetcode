# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # state variable (TreeNode, string of all the nodes so far)
        # Let's use DFS to do it
        if root is None: return 0
        
        # initialize with root node and empty string
        stack = [(root,"")]
        
        total_sum = 0

        while stack:
            node, root_to_lead_string = stack.pop()

            root_to_lead_string += str(node.val)

            # if reach leaf node
            if node.left is None and node.right is None:
                total_sum += int(root_to_lead_string)

            # left
            if node.left:
                stack.append((node.left, root_to_lead_string))

            # right 
            if node.right:
                stack.append((node.right, root_to_lead_string))

        return total_sum


