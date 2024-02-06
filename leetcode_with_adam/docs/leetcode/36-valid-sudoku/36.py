from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 vertical scan, 9 horitonal scan, 9 3x3 grid scan
        def is_horizontal_valid(matrix):
            for row in matrix:
                hashmap = set()
                for item in row:
                    if item in hashmap:
                        return False
                    hashmap.add(item)
                    print(hashmap)
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
                    if matrix[j][i] in hashmap:
                        return False
                    hashmap.add(matrix[j][i])
            return True

        def is_sub_box_valid(matrix):
            for x in range(0, 9, 3):
                for y in range(0, 9, 3):
                    hashmap = set()
                    for i in range(3):
                        for j in range(3):
                            if matrix[x + i][y + j] in hashmap:
                                return False
                            hashmap.add(matrix[x + i][y + j])
            return True

        res = False
        if (
            is_sub_box_valid(board)
            and is_vertical_valid(board)
            and is_horizontal_valid(board)
        ):
            res = True

        print(is_horizontal_valid(board))
        print(is_vertical_valid(board))
        print(is_sub_box_valid(board))

        return res


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
a = Solution()

a.isValidSudoku(board)
