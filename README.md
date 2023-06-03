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
- [x]  [104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
	- [x] [BFS solution. It's easier with BFS. Just set a counter](./LeetCode/104-maximum-depth-of-binary-tree/104-BFS.py)
	- [ ] recursion
	- [ ] DFS to really work with ur brain on tracking depth. 
- [ ]  [110 Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
  - [ ] bottom-up
  - [ ] top-down  
- [x]  [111 Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
  - First thought: BFS with auxillary DS (stack) to track all leaf node's height. [Solution](./LeetCode/111-minimum-depth-of-binary-tree/111-BFS.py).
  - optimized: If we use BFS, the first encounter of leaf node will have the minimum depth, [solution here](./LeetCode/111-minimum-depth-of-binary-tree/111-BFS-optimized.py).
- [x]  [617 Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees)
  - BFS on left tree. Left tree absorb right tree. The control flow is kinda tricky. [Solution here](./LeetCode/617-merge-two-binary-trees/README.md).  
- [ ]  [543 Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
- [ ]  [563 Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt)
- [x]  [226 Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
  - [BFS but insert right node first at each level](./LeetCode/226-invert-binary-tree/README.md)


## Binary Search Tree Problems
---
- [x] [700 Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)
  - very basic BST, [solution](./LeetCode/700-search-in-a-binary-search-tree/700.py)
- [x] [653 Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
  - two sum variation. Instead of array + hash --> tree + hash; instead of iteration to traverse array, we do inorder traversal (or others). [Solution here](./LeetCode/653-two-sum-IV-input-is-a-BST/653-two-sum-BST.py) 
- [x] [530 Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
  - trick is to use the property of BST. in-order depth first DFS on BST will output sorted list. [Solution here](./LeetCode/530-minimum-absolute-difference-in-BST/530-DFS-inorder.py)
- [x] [938 Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)
  - DFS to a list, then traverse. [solution here](./LeetCode/938-range-sum-of-BST/938.py). 
- [ ] [450 Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [ ] [669 Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree)
- [ ] [701 Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree)
- [x] [230 Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)
  - in order traversal, [solution here](./LeetCode/230-kth-smallest-element-in-BST/230-in-order-DFS.py)
- [ ] [1305 All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees)
  - $O\left((m+n)log(m+n)\right)$ in time and $O(m+n)$ in space by in-order traversal twice then merge with quick sort, kinda dumb but solution is [here](./LeetCode/1305-all-elements-in-two-binary-search-trees/1305-dumb-solution.py)
  - [ ] this question must be solved with optimal solution. Go back to this when i have more time.

## Path Problems
---
- [x] [257 Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
  - [DFS, iterative solution with a stack of tuple](./LeetCode/257-binary-tree-paths/257-iterative.py). Also avoid overclustering heap with intermediate string causes by `+`, use `join()` instead, reason [here](./LeetCode/257-binary-tree-paths/README.md).
- [x] [112 Path Sum](https://leetcode.com/problems/path-sum)
  - DFS solution with a stack of tuple, the tuple carries (node, currSum), node is for traversing and providing value for this iteration, currSum carries the state variable of path sum until this current node. [Solution here](./LeetCode/112-path-sum/112-DFS.py).
  - [ ] Alternatively, you could use BFS to solve.
- [x] [113 Path Sum II](https://leetcode.com/problems/path-sum-ii)
  - [DFS solution here](./LeetCode/113-path-sum-II/113_DFS.py), a tuple again but tracking three state 
- [ ] [129 Sum root to leaf numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
- [ ] [124 Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [ ] [437 Path Sum III](https://leetcode.com/problems/path-sum-iii)
- [ ] [1457 Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

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