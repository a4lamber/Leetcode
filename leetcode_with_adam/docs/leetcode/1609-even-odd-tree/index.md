---
tags:
    - Tree
    - Breadth-First Search
    - Binary Tree
---

# 1609 Even Odd Tree

typical tree BFS with queue, the trick is

- maintain一个flag to determine odd or even layer and perform checks on
    - `odd layer`: strictly decreasing and all even numbers
    - `even layer`: strictly increasing and all odd numbers

!!! note "Time complexity"
    `Time complexity:` $O(n)$ where `n` is the number of nodes in the tree. We need to visit all nodes, plus sort all nodes in every layer.

    `Space complexity:` In the last layers of a binary tree with height $h$, we have $2^h=k$ and $k$ is the number of nodes in the last layer. In worst case scenario, the binary tree is full, so we have the relationship between the number of nodes $n$ and the height of the tree $h$ as $n=2^h-1$. So $k\approx n$, and the space complexity is $O(n)$.


## Approach 1 BFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # 1. BFS, left to right scan with queue
        # 2. check if odd level increasing order
        # 3. check if even level decreasing order
        # at most
        # lvl 0 : 2**0 = 1
        # lvl 1 : 2**1 = 2
        # lvl 2: 2**2 = 4

        level = 0
        queue = collections.deque([root])
        
        while queue:
            array = []
            
            for _ in range(len(queue)):
                # in case this lvl is not full                       
                curr = queue.popleft()
                array.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            # reverse flag
            odd = False if level % 2 == 0 else True
            
            if odd:
                # we at odd level, strictly decreasing, all even number
                for i in range(len(array)-1):
                    if array[i+1] >= array[i] or array[i] % 2 == 1:
                        return False
                    
                if array[len(array)-1] % 2 == 1: return False

            else:
                # we at even level, strictly increasing, all odd number
                for i in range(len(array)-1):
                    if array[i+1] <= array[i] or array[i] % 2 == 0:
                        return False
                if array[len(array)-1] % 2 == 0: return False

            # update the lvl
            level += 1
        
        return True
```

slight improvement can be made for how to maintain the flag variable by `odd = not odd` instead of doing extra work to check if the level is odd or even by modulus operation `%` and maintain a counter.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # 1. BFS, left to right scan with queue
        # 2. check if odd level increasing order
        # 3. check if even level decreasing order
        # at most
        # lvl 0 : 2**0 = 1
        # lvl 1 : 2**1 = 2
        # lvl 2: 2**2 = 4
        
        odd = False
        level = 0
        queue = collections.deque([root])
        
        while queue:
            array = []
            
            for _ in range(len(queue)):
                # in case this lvl is not full                       
                curr = queue.popleft()
                array.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            
            if odd:
                # we at odd level, strictly decreasing, all even number
                for i in range(len(array)-1):
                    if array[i+1] >= array[i] or array[i] % 2 == 1:
                        return False
                    
                if array[len(array)-1] % 2 == 1: return False

            else:
                # we at even level, strictly increasing, all odd number
                for i in range(len(array)-1):
                    if array[i+1] <= array[i] or array[i] % 2 == 0:
                        return False
                if array[len(array)-1] % 2 == 0: return False

            # toggle flag
            odd = not odd
        
        return True
```