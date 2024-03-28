# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 以左边的tree作为basis, 不断添加右边的东西进入;
        if root1 is None:
            return root2

        queue = deque([(root1,root2)])

        while queue:
            for _ in range(len(queue)):
                p,q = queue.popleft()
                
                # both are None
                if p is None or q is None: continue
                # accumulate the sum
                p.val += q.val

                # 如果left tree's children is None, 则copy!
                if p.left is None:
                    p.left = q.left
                else:
                    queue.append((p.left,q.left))
                
                if p.right is None:
                    p.right = q.right
                else:
                    queue.append((p.right,q.right))
        
        return root1
                


                
