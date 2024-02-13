---
tags:
    - Dynamic Programming
    - Math
    - Combinatorics
---
# [62 Unique Paths](https://leetcode.com/problems/unique-paths/description/)



## Approach 1: DP

!!! note note
    time complexity: O(m*n)
    space complexity: O(m*n)

### DP三宝

#### DP定义

`dp[i][j]`：表示从起点`(0,0)`到达`(i,j)`所有路径数.

#### DP初始化

起点`dp[0][0]`必然是1, 因为只有一种可能性. 必然是由于只能往右或者往下走，所以第一行第一列都是1. 

$$
\begin{equation}
dp[i][j] = \begin{cases}
    1, & \text{if } i=0 \text{ or } j=0\\
    0, & \text{otherwise}
\end{cases}
\end{equation}
$$

#### DP状态转移

Since the robot can only move right and down, your matrix will be updated from top or left.

$$
\begin{equation}
dp[i][j] = \begin{cases}
    dp[i-1][j] + dp[i][j-1], & \text{if } i>0 \text{ and } j>0\\
    1, & \text{if } i=0 \text{ or } j=0
\end{cases}
\end{equation}
$$

### Code Implementation

!!! tip Tip
    这里用了`defaultdict`来初始化`dp`，instead of array, 这样可以避免处理boundary的问题，超过边界直接默认为0了.

```python
from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[(i,j)]: number of possible ways to reach to the grid[m][n]
        # initial condition
        # dp[(i,0)] = 1, dp[(0,j)] = 1
        # state transition function:
        #   dp[(i,j)] = dp[(i-1,j)] + dp[(i,j-1)]

        dp = defaultdict(int)
        for i in range(m):
            dp[(i,0)] = 1

        for i in range(m):
            for j in range(1,n):
                dp[(i,j)] = dp[(i-1,j)] + dp[(i,j-1)]
                
        return dp[(m-1,n-1)]
```
你甚至可以省略初始化那一步，因为我们的信息都是从左上角开始的，所以只要从左上角开始horizontal或者vertical的遍历就可以了.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
```


## Approach 2: DP, space optimized

发现上面的DP其实只用到了上一行的信息，所以我们可以优化空间复杂度, reduce to $O(m)$ or $O(n)$, 根据你选择的horizontal scan or vertical scan.

!!! note note
    time complexity: O(m*n)
    space complexity: O(n)

### Code Implementation

```python
from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1: return 1

        prev = [1 for _ in range(m)]
        curr = [0 for _ in range(m)]

        for j in range(1,n):
            for i in range(m):
                # update curr
                if i == 0:
                    curr[i] = prev[i]
                else:
                    curr[i] = prev[i] + curr[i-1]
        
            prev = curr.copy()
        
        return curr[-1]
                
```