---
tags:
  - Tree
  - Depth-First Search
  - Breadth-First Search
  - Binary Tree
---

# [100 Same Tree](https://leetcode.com/problems/same-tree/description/?envType=daily-question&envId=2024-02-26)

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example
```
    1
   / \
  2   3

VS 

    1
   / \
  3   2
```

```
output: False
```

## Approach 1 BFS


If a tree `p` and a tree `q` are the same, they must possesses the following two conditions

- **Condition1**: tree `p` and `q` has the same structure
- **Condition2**: values in p and q are the same.

If order to do that, we need to do some sort of traversal to examine the above two conditions. The takeaway for this problem is illustrated in the box in the diagram below

- if two nodes are both `None`, (still valid but we don't want to append None in the queue, so `continue`)
- if one of them not None while the other is None, **condition 1 not met.**
- if value is not same, **condition 2 not met.**

Now, you should have a clearer picture on the thought process. 

![](./assets/100_same_tree.excalidraw.png)


```python
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
```

## Approach 2 Recursive

```python
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
```