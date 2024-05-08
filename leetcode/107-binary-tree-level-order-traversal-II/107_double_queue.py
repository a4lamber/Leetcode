# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if root is None: return []

        # BFS then reverse
        levels = deque()
        queue = deque([root])

        while queue:
            curr_level = []

            for _ in range(len(queue)):
                # pop and append 
                curr = queue.popleft()
                curr_level.append(curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            # append to the left
            levels.appendleft(curr_level)

        return levels
            
        