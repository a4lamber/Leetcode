---
tags:
    - array
    - matrix
    - hash table
---
# [36 Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)


等价转换三条规则:
- every row must contain the digits 1-9 without repetition.
- every column must contain the digits 1-9 without repetition.
- every of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

然后根据三条规则，做三次matrix traversal，分别检查是否valid, 虽然可以优化到one pass, 但是asymptotic time complexity没有变化. 

$O(n^2)$ in time complexity, $O(n)$ space complexity. 当然，你也可以argue说是$O(1)$ in both time and space complexity, 因为我们只是用了一个hashmap来存储，且循环数固定为9 * 9 = 81.

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 vertical scan, 9 horitonal scan, 9 3x3 grid scan
        def is_horizontal_valid(matrix):
            for row in matrix:                
                hashmap = set()
                for item in row:                        
                    if item != "." and item in hashmap:
                        return False                        
                    hashmap.add(item)
            
            return True

        
        def is_vertical_valid(matrix):
            """
            first pass
            (0,0),(1,0),(2,0)...
            2nd pass
            (0,1),(1,1),(2,1)...
            """
            for i in range(len(matrix)):
                hashmap = set()
                for j in range(len(matrix)):
                    if matrix[j][i] != "." and matrix[j][i] in hashmap:
                        return False
                    hashmap.add(matrix[j][i])            
            return True
        
        def is_sub_box_valid(matrix):
            for x in range(0,9,3):
                for y in range(0,9,3):
                    hashmap = set()
                    for i in range(3):
                        for j in range(3):
                            if matrix[x+i][y+j] != "." and matrix[x+i][y+j] in hashmap:
                                return False
                            hashmap.add(matrix[x+i][y+j])
            return True
        
        res = False
        if is_sub_box_valid(board) and is_vertical_valid(board) and is_horizontal_valid(board):
            res = True

        return res
```
