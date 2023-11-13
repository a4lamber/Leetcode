# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursion base cases
        # 1. 两个都是none
        # 2. 一个是none另一个不是none
        # 3. 两个都是value, 但不等
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        # program如果还能执行到这里，只有p.val == q.val的情况了,这种情况就继续挖下去, 不return boolean, return function

        # 两个只要有任何一个返回的是false, 那就是false
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)


