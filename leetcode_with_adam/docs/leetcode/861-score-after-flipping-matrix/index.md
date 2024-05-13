---
tags:
    - Array
    - Greedy
    - Matrix
    - Bit Manipulation
---

# [861 Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/description/?envType=daily-question&envId=2024-05-13)


## Approach 1 With Flipping

Consider an binary `1000`, if we flip it, it turns into `0111`, then the values are:

- `1000` = 8
- `0111` = 7

So, it is clear that we should flip the first digit to 1 if it is 0.

So the algorithm is:

- examine each row, if the first digit is 0, flip the entire row
- examine each column, if the number of 0 is more than the number of 1, flip the entire column.
- calculate the sum

!!! note "Time Complexity"
    
    - time complexity is $O(m + 2mn)$, where $m$ is the number of rows and $n$ is the number of columns.
    - space complexity is $O(1)$


```python
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        # scan each row to flip
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        # scan each column
        res = 0
        for j in range(n):
            count = {1:0,0:0}
            for i in range(m):
                count[grid[i][j]] += 1
            
            if count[0] > count[1]:
                # we flip
                for i in range(m):
                    grid[i][j] = 0 if grid[i][j] == 1 else 1

                count[1],count[0] = count[0],count[1]
            
            res += count[1] * 2**(n-j-1)
        return res
```

## Approach 2 W/O Flipping

You can get the result without flipping the matrix. The key is to understand the pattern of the matrix.

- The first column should be all 1s, to maximize the score.
- The rest of the columns should have more 1s than 0s. If allowed, We can "flip" the column if the number of 0s is more than the number of 1s. W/O flipping, we can just count the number of values that are different from the first column.



```python
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        # 1st column
        res = m * 2**(n-1)
        # other columns
        for j in range(1,n):
            count = 0
            # 计算和首字母相同的个数
            for i in range(m):
                if grid[i][j] != grid[i][0]:
                    count += 1

            res += max(count,m-count) * 2**(n-j-1)

            print(res)
        return res
```