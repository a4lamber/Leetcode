# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            current_size = len(queue)
            for _ in range(current_size):
                curr = queue.popleft()
                if curr:
                    if curr.left: 
                        queue.append(curr.left)
                    if curr.right: 
                        queue.append(curr.right)
            # 每过一层 + 1
            depth += 1
        
        return depth

  
        
