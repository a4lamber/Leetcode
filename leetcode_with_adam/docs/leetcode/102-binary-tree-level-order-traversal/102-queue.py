# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []

        queue = deque([root])
        levels = []

        while queue:
            levels.append([]) # 加新的一层
        
            for i in range(len(queue)):
                current_node = queue.popleft()
                levels[-1].append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
            
        return levels
