# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # brute force, where m is # of nodes in root1 while n the # of nodes in root2
        # time complexity: O((n+m)log(m+n)) space: O(m+n), 还是需要sort, 怎么可以不sort?
        def helper(root):
            res = []
            stack = []
            curr = root

            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            
            return res

        solution = helper(root1) + helper(root2)
        solution.sort()

        return solution
                
        
