# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        stack = [(root, str(root.val))]

        while stack:
            # unpack stack
            node, path = stack.pop()
            # reach leaf node
            if not node.left and not node.right:
                # 只在reach leaf node时，写入
                paths.append(path)
            
            if node.left:
                stack.append((node.left, '->'.join([path, str(node.left.val)])))
                # stack.append((node.left, path + '->' + str(node.left.val)))

            if node.right:
                stack.append((node.right, '->'.join([path, str(node.right.val)])))
                # string immutable, the above
                # stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths