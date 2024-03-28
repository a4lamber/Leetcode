---
tags:
    - Tree
    - Hash Table
    - Breadth-first Search
    - Binary Tree
---

# [314 Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/)

2D matrix of a tree! 这题的解法都是bfs-based, 

- approach 1 BFS + Sorting, O(nlogn) time complexity, O(n) space complexity. 维护一个list of tuple (node.val, col), sort by col, 之后再append到res里面.
- approach 2 BFS no sorting, 是最优解. O(n) time complexity, O(n) space complexity without sorting. 很巧妙且实用的trick.

## Approach 1 BFS + Sorting

Intuition:

- create a score tracking system, if move left -= 1, if move right += 1

在BFS traverse的时候，就可以想到在maintain一个tuple of (node, score), 之后sort by score即可. 然后再根据score来append到res里面.

Dry run would be 

```
    3
   / \
  9  20
    /  \
   15   7

[(3,0),(9,-1),(20,1),(15,0),(7,2)]   

then we sort it
[(9,-1),(3,0),(15,0),(20,1),(7,2)]
    
we organize it to
[[9],[3,15],[20],[7]]
```

!!! note "Code Implementation"
    第一次看到时候，想到list of tuples.

    ```python
    from collections import deque
    class Solution:
        def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return root
            
            queue = deque([(root,0)])
            level = []

            while queue:
                for _ in range(len(queue)):
                    curr,curr_pos = queue.pop()
                    level.append((curr,curr_pos))
                    if curr.left:
                        queue.appendleft((curr.left,curr_pos-1))
                    if curr.right:
                        queue.appendleft((curr.right,curr_pos+1))
                
            level.sort(key=lambda x:x[1])
            node,prev = level[0]
            res = [[node.val]]

            for i in range(1,len(level)):
                node,curr = level[i]
                if curr == prev:
                    res[-1].append(node.val)
                else:
                    res.append([node.val])            
                prev = curr
            return res
    ```


list of tuple这样写起来太麻烦了，sort之后还需要explicitly的再次遍历，很clumsy, 有一个优化readibility的方法:

> use hash table `defaultdict(list)` to store the column as key and list of nodes as value. Since we BFS, each `hashtable[key]` will remain sorted.

!!! note "小优化"
    ```python
    from collections import deque,defaultdict
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            """
            intuition:
                - create a score tracking system, if move left -= 1, if move right += 1
            dry run:
                [(3,0),(9,-1),(20,1),(15,0),(7,2)]        
            """
            if not root:
                return root
            
            queue = deque([(root,0)])
            hashtable = defaultdict(list)

            while queue:
                for _ in range(len(queue)):
                    curr,curr_col = queue.pop()
                    hashtable[curr_col].append(curr.val)
                    if curr.left:
                        queue.appendleft((curr.left,curr_col - 1))
                    if curr.right:
                        queue.appendleft((curr.right,curr_col + 1))
            
            return [hashtable[x] for x in sorted(hashtable.keys())]
    ```


## Approach 2 BFS no Sorting

跟着approach 1 minor 优化的思路，怎么可以进一步优化呢? 我们发现我们最后获得的column, 肯定是contiguous integer, 也就是说我们可以用一个min_col和max_col来track我们的column的范围, 之后不需要sort, 直接iterate min_col to max_col即可.

!!! tip
    维护两个变量，min_col和max_col就能交换一个sort的时间复杂度. 超值!
    
```python
from collections import deque,defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        intuition:
            - create a score tracking system, if move left -= 1, if move right += 1
        dry run:
            [(3,0),(9,-1),(20,1),(15,0),(7,2)]        
        """
        if not root:
            return root
        
        queue = deque([(root,0)])
        hashtable = defaultdict(list)
        min_col = max_col = 0
        while queue:
            for _ in range(len(queue)):
                curr,curr_col = queue.pop()
                hashtable[curr_col].append(curr.val)
                min_col = min(min_col,curr_col)
                max_col = max(max_col,curr_col)                
                if curr.left:
                    queue.appendleft((curr.left,curr_col - 1))
                if curr.right:
                    queue.appendleft((curr.right,curr_col + 1))
        
        return [hashtable[x] for x in range(min_col,max_col+1)]        
```
