# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []

        queue = deque([root]) 
        levels = []
        # if flag is even left to right; if flag odd, right to left
        reverse_flag = 0 

        while queue:
            levels.append([])

            for _ in range(len(queue)):
                node = queue.popleft()
                levels[-1].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if reverse_flag % 2 == 1:
                levels[-1].reverse()
            reverse_flag += 1
        
        return levels
                                    



