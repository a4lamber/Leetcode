# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        res = []

        while stack or curr:
            # 只要还能往left走，就走，边走边append值和stack node, 因为还要回来
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            # 左边走完了，现在返回上级，往右走一次，end of the curr iter, 下面看能不能继续往左走
            curr = stack.pop()
            curr = curr.right
        
        return res

