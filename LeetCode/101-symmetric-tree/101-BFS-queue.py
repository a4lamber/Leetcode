# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 思路1: in order travelsal后，结果reverse则是symmertirc, 反例[1,2,2,2,null,2]
        # 思路2: 同时BFS两个tree: root.left, root.right
        # 能满足性质left正常BFS, right在append数据的时候，先加入右边再加入左边
        p = root.left
        q = root.right

        queue = deque([(p,q)])

        while queue:
            p,q = queue.popleft()

            if p is None and q is None:
                continue

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            # 俩是一定相等了
            queue.extend([(p.left,q.right),(p.right,q.left)])
        
        return True


             



        

