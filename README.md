# LeetCode Grind Journey

> Need a systematic way to grind LC so i have more time to work on other interesting stuff.


*Table of contents*
- [LeetCode Grind Journey](#leetcode-grind-journey)
- [Tree](#tree)
	- [Depth-first Traversal](#depth-first-traversal)
	- [Level-first Traversal](#level-first-traversal)
	- [Others](#others)
	- [Binary Search Tree Problems](#binary-search-tree-problems)
	- [Path Problems](#path-problems)
	- [Construct BT \& BST](#construct-bt--bst)
- [Reference](#reference)



# Tree

Tree problems on LC are categorized into two fold
- depth first approach
- breadth first approach

## Depth-first Traversal

Tree depth-first traversal is summarized as:
- recursive solution is the easiest
- iteration solution relies on auxillary data structure `stack` to store the nodes in a order that corresponds to the visiting order


 - [x] [94 Binary Tree Inorder traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
	- [ ] recursion
	- [x] [iteration with stack](https://github.com/a4lamber/Leetcode/blob/d006a304d8d861819ee1e5f1a02eb30988e51d89/LeetCode/94-binary-tree-inorder-traversal)
	- [ ] morris
- [x] [144 Binary Tree Preorder traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
	- [ ] recursion
	- [x] [iteration with stack](https://github.com/a4lamber/Leetcode/blob/d04c98fa7e2d0f752301b4bee262be8799d2e996/LeetCode/144-binary-tree-preorder-traversal)
	- [ ] morris
- [x] [145 Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
	- [ ] recursion
	- [x] iterative solution
		- [approach1: reverse modified pre-order](LeetCode/145-binary-tree-postorder-traversal/145-iteration-flip-modified-pre-order.py): post-order traversal (left, right, root) if we reverse it, it's (root, right, left). This becomes "modified" pre-order. Merge the solution to the some knowledge we already know. 
	- [ ] morris

## Level-first Traversal

level-first traversal typically,
- uses `queue` as auxillary data structure to temporarily store nodes in the current level

- [x] [102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
  - BFS, something you should mark in your head. [solution here](LeetCode/102-binary-tree-level-order-traversal/102-queue.py)
- [x] [103 Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
	- trick在于有一种方法计算在目前在哪一层，for a perfect tree, 1 --> 2 --> 4, 可以每一次append完children之后，求一下总数, [solution](LeetCode/103-binary-tree-zigzag-level-order-traversal/103-queue.py) is here
- [x] [107 Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
  - Using regular DFS, but we use deque for output `res = deque()`. We `appendleft` at the end of each layer. [Solution](./LeetCode/107-binary-tree-level-order-traversal-II/107_double_queue.py) and [note](./LeetCode/107-binary-tree-level-order-traversal-II/README.md) are here.


## Others
---
- [x]  [100 Same Tree](https://leetcode.com/problems/same-tree/)
	- [x] recursion
	- [x] [BFS with queue](./LeetCode/100-same-tree/README.md)
- [x]  [101 Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
	- [x] [BFS solution](./LeetCode/101-symmetric-tree/README.md), symmetric tree is very similar with same tree. Just remember comparing medial sides then lateral side.
- [ ]  [104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
	- [x] BFS
		-  BFS solution is easier，不需要反复改变current depth和打擂台找maximum depth
	- [ ] recursion
	- [ ] DFS to really work with ur brain on tracking depth. 
- [ ]  [110 Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [ ]  [111 Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [ ]  [617 Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees)
- [ ]  [543 Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [ ]  [563 Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt)
- [ ]  [226 Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)


## Binary Search Tree Problems
---
- [ ] [700 Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)
- [ ] [653 Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
- [ ] [530 Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
- [ ] [938 Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)
- [ ] [450 Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [ ] [669 Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree)
- [ ] [701 Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)
- [ ] [230 Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)
- [ ] [1305 All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees)

## Path Problems
---
- [ ] [257 Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
- [ ] [112 Path Sum](https://leetcode.com/problems/path-sum)
- [ ] [113 Path Sum II](https://leetcode.com/problems/path-sum-ii)
- [ ] [129 Sum root to leaf numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
- [ ] [124 Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [ ] [\*437 Path Sum III](https://leetcode.com/problems/path-sum-iii)
- [ ] [\*1457 Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

## Construct BT & BST
- [ ] [105 Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)
- [ ] [106 Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal)
- [ ] [889 Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal)
- [ ] [108 Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)
- [ ] [1008 Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal)





# Reference
- https://runestone.academy/ns/books/published/pythonds/index.html
- https://blog.csdn.net/Holmofy/article/details/76401074
- [dictionary of algorithms and data structure](https://xlinux.nist.gov/dads/) This site has many definition for terminology used in data structure, especially u r confused about data structure in an academic setting.