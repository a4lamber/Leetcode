---
tags:
    - Array
    - Matrix
    - Dynamic Programming
---

# [931 Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)

classic 2D dp problem.

## Approach 1: bottom-up

!!! note "time complexity"
    
    - $O(n^2)$ in time
    - $O(n^2)$ in space since we store the path sum of each cell.

这一题首先先画个树，我们发现, 可以分类讨论

|-|diagonally left|down|diagonally right|
|-|-|-|
|first column|🚫|✅|✅|
|last column|✅|✅|🚫|
|other columns|✅|✅|✅|

那这样的话，我们就可以dp三部曲了.

!!! tip DP
    Definition of DP:
    > `dp[i][j]: 表示到达cell[i][j]的最小路径和`

    Initialization:
    
    $$
    dp[0][j] = matrix[0][j] \quad \text{for} \quad j \in [0,n)
    $$

    State Transition:

    $$
    dp\left[i\right][j] = \begin{cases}
    matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])\quad j=0\\
    matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])\quad j \in [1,n)\\
    matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1])\quad j=n\\
    \end{cases}
    $$
    where i >= 1

### Code Implementation

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[i][j] the min path sum reach cell[i][j]
        n = len(matrix)
        
        # edge case
        if n == 1: return matrix[0][0]

        dp = [[0 for j in range(n)] for i in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # scan vertical
        for i in range(1,n):
            # scan horizontally
            for j in range(n):
                # left boundary nodes
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                    continue

                # right bounday nodes
                if j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j])
                    continue

                # interior nodes
                dp[i][j] = matrix[i][j] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        
        return min(dp[-1])
```

## Approach 2: bottom-up with space optimization

In state transition function, we realize that we only need the previous row to calculate the current row. Therefore, we only need to maintain two rows of dp array.


```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        # initialize first row
        prev = [val for val in matrix[0]]
        curr = [0 for _ in range(n)]

        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    curr[j] = matrix[i][j] + min(prev[j],prev[j+1])
                elif j == n-1:
                    curr[j] = matrix[i][j] + min(prev[j-1],prev[j])
                else:
                    curr[j] = matrix[i][j] + min(prev[j-1],prev[j],prev[j+1])
            
            prev = curr.copy()
        return min(curr)
```