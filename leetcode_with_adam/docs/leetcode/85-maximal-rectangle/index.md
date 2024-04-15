---
tags:
    - Array
    - Matrix
    - Dynamic Programming
    - Monotonic Stack
    - Stack
---
# 85 Maximal Rectangle

和[84 largest rectangle in histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)算是姐妹题了. 这题还没完全吃透，需要再看看。

## Approach 1 DP 

为了计算面积最大的矩阵，area = width * height. 我们有两种方法求:

- 保存每个点的最大高度，然后迭代所有可能的宽度
- 保存每个点的最大宽度，然后迭代所有可能的高度
- 枚举所有可能性(暴力解)


这里我们选择第二种方法，保存宽度.

> `dp[i][j]` is defined as the maximum width of the rectangle that ends at `(i,j)`.

It's state transition function is 

$$
\begin{equation}
\text{{dp}}[i][j] = \begin{cases} 
0 & \text{if } \text{{matrix}}[i][j] = "0" \\
1 & \text{if } j = 0 \text{ (i.e., first column)} \\
\text{dp}[i][j-1] + 1 & \text{otherwise} \\
\end{cases}
\end{equation}
$$


!!! tip
    有时候，dp的定义不一定是最终的答案，但是可以帮助我们找到最终的答案。这里的`dp[i][j]`是最大宽度，但是最终的答案是面积，所以我们要在dp的基础上，再次计算面积。我fell into the trap of 想直接定义`dp[i][j]`为面积，但是这样的话，`dp[i][j]`的状态转移方程就无法定义了.

接下来，在每一个time step, 我们需要往上traversal to calculate the histogram, 如下图.

这是一个越往上，width条件越严苛的问题，所以我们要在每一个time step, 更新width的值，取最小值,高度则递减。

!!! note "复杂度分析"

    - time complexity: $O(m^2n)$, 由于我们需要往上traverse一个`len(matrix)`. 
    - space complexity: $O(mn)$.


### Code Implementation

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]: maximum width ends at (i,j).
        state transition function:
            dp[i][j] = 0 if matrix[i][j] = "0"
                     = 1 if j == 0 i.e. first column
                     = dp[i][j-1] + 1 otherwise        
        """
        maxarea = 0
        m,n = len(matrix),len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                # consecutive width so far
                # j==0,第一列为0
                if j:
                    width = dp[i][j-1] + 1
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = width = 1
                # width = dp[i][j] = dp[i][j-1] + 1 if j else 1

                # 往上计算histogram
                # height: i-k+1
                for k in range(i,-1,-1):
                    # 越往上，width条件越严苛
                    width = min(width,dp[k][j])
                    maxarea = max(maxarea,width * (i-k+1))
        return maxarea
```

## Approach 2 DP maximum height


```python

```

