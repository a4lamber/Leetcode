

# Intuition

As for brute force solution, we need to iterate every single possible submatrics and sum each submatix to see if it equals to target. This will take $O(n^4)$ time complexity.

Now we need to think about a trick to solve it and its prefix-sum.

# Approach

## Prefix Sum matrix的构建
Prefix sum, 这个trick可以减少很多重复的计算，定义一个`prefix_sum[i][j]`, 

> `prefix_sum[i][j]` = sum of all elements in the submatrix from `(0,0)` to `(i,j)` (top left to bottom right)

甚至在计算prefix_sum时，可以用到这个trick, 

$$
prefix\_sum[i][j] = matrix[i][j] + prefix\_sum[i-1][j] + prefix\_sum[i][j-1] - prefix\_sum[i-1][j-1]
$$


## Hashmap的构建

首先还是要延伸一下[560 subarray sum equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)中的prefix sum + hash思路for array, 这里是其2D延伸.

> 在一个矩阵当中，任何一个submatrix都可以由两个其它submatrix的差值来构建出来.

也就是说，任何一个submatrix的和，都可以由其它两个submatrix的和的差值来构建出来. 这也是prefix sum的基本理论. 但我们看看这两个submatix有什么要求呢? 

For a matrix with (r1,c1) as top left corner and (r2,c2) as bottom right corner, 我们只能用,
- `matrix 1`: 以(0,c1)为左上角，(r2,c2)为右下角的matrix (大的那个)
- `matrix 2`: 以(r1-1,c1)为左上角，(r1,c2)为右下角的matrix (小的那个)




```python
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # prefix_sum矩阵: 储存以(i,j)为bottom right corner, (0,0)为top left corner为定义的矩阵之和
        # 

        ROWS,COLS = len(matrix), len(matrix[0])
        prefix_sum = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # O(m*n)
        for r in range(ROWS):
            for c in range(COLS):
                top = prefix_sum[r-1][c] if r > 0 else 0
                left = prefix_sum[r][c-1] if c > 0 else 0
                top_left = prefix_sum[r-1][c-1] if c > 0 and r > 0 else 0
                prefix_sum[r][c] = matrix[r][c] + top + left - top_left

        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1,ROWS):
                # initialize an empty hashmap with base case 0 -> 1
                # the hashmap count is only valid for matrix with r1, r2 锁死了row, 但是col可以变的情况
                count = defaultdict(int)
                count[0] = 1
                for c in range(COLS):
                    # cur_sum:以(r1,0)为左上角，(r2,c)为右下角的matrix的值                   
                    cur_sum = prefix_sum[r2][c] - (
                        prefix_sum[r1-1][c] if r1 > 0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    # update accumulative sum
                    count[cur_sum] += 1
        return res
```