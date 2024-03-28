# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None: return None

        inverted_root = TreeNode(val = root.val)
        inverted_queue = deque([inverted_root])

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                inverted_curr = inverted_queue.popleft()

                # right append left, left append right
                if curr.right: 
                    queue.append(curr.right)
                    inverted_curr.left = TreeNode(curr.right.val)
                    inverted_queue.append(inverted_curr.left)

                if curr.left: 
                    queue.append(curr.left)
                    inverted_curr.right = TreeNode(curr.left.val)
                    inverted_queue.append(inverted_curr.right)

        
        return inverted_root


