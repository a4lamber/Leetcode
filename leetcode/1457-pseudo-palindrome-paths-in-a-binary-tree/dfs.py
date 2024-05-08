# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # Pseudo-palindrom: 这个iterable的anagram, 能满足palindrom condition
        self.counter = 0

        def is_pseudo_palindrome(path: dict) -> bool:
            """check if path is a pseudo-palindrome"""
            odd_counter = 0
            for count in path.values():
                if count % 2 == 1:
                    odd_counter += 1

            if odd_counter == 1 or odd_counter == 0:
                return True
            else:
                return False

        def helper(node: Optional[TreeNode], path: dict):
            if node:
                path[node.val] += 1
                # if leaf node
                if not node.left and not node.right:
                    if is_pseudo_palindrome(path):
                        self.counter += 1

                helper(node.left, path)
                helper(node.right, path)
                ## reach leaf node, go back one layer (往回走一层)
                path[node.val] -= 1

        helper(root, defaultdict(int))

        return self.counter
