# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS --> queue
        # the condition for minimum depth is that for a node P
        # P.left and P.right are both None

        if root is None: return 0

        queue = deque([root])
        depth = 1
        leaf_depth = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                # if leaf node
                if node.left is None and node.right is None:
                    leaf_depth.append(depth)
            
            depth += 1

        return min(leaf_depth)
        



