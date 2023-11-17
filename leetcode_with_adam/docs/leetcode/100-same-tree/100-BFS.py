# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Approach 1
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS, tuple in list
        queue = deque([(p,q)])

        while queue:
            node_a,node_b = queue.popleft()
            if node_a is None and node_b is None:
                # 都是none, 不放入queue
                continue
            elif node_a is None or node_b is None:
                return False
            elif node_a.val != node_b.val:
                return False
            # 剩下都是数值相等的情况了
            queue.extend([(node_a.left,node_b.left),(node_a.right,node_b.right)])
        return True


# Approach 2  
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p,q])
        
        # pass
        while queue:
            a = queue.popleft()
            b = queue.popleft()

            if a is None and b is None: continue
            if a is None or b is None: return False
            if a.val != b.val: return False

            # when gets here, a and b are both TreeNode
            queue.append(a.left)
            queue.append(b.left)
            queue.append(a.right)
            queue.append(b.right)

        return True