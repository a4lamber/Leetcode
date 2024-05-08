# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []

        queue = deque([root])
        levels = []

        while queue:
            levels.append([])
            temp_length = len(queue) # 虽然直接写在range()里面少一个variable, 但queue的长度随着iteration变化而变化，bette store 
it outside
            # iterate for the # of nodes at current queue
            for _ in range(temp_length):
                # visit the leftmost node in the queue
                node = queue.popleft()
                levels[-1].append(node.val)

                # append from the right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        levels.reverse()
        
        return levels
                


            
