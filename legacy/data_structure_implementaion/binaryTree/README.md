# Readme
---

Binary tree has the properties that it only has have 2 child nodes.

Binary search tree is a special case of binary tree that left child less than parent and right node greater than parent node.

Binary search tree has
- breadth first search
- depth first search
  - in order traveral (left sub tree, root, right sub tree)
  - pre order traversal (root, left sub tree, right sub tree)
  - post order traversal (left sub tree, right sub tree, root)

Whether you place your root node between left adn right sub tree are the traversal node


## Problem 1 (from codebasics)

Add the following methods to BinarySearchTreeNode class

```
1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
```

[solution](./solution/binary_tree.py)