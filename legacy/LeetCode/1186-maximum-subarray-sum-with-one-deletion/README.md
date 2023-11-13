# Approach 1: Bottom up constant space

## DP定义,状态转移方程和初始化

- `DP[0][i]`: maximum subarray ending on `arr[i]`. 也就是一定不删. 状态转移方程如下:
$$
\begin{align}
\rm{}DP[0][i] &= max(DP[0][i-1] + arr[i],arr[i])\\
\rm{}DP[0][0] &= arr[0]
\end{align}
$$
这个很好理解，没什么可说的,就是maximum subarray中的定义

- `DP[1][i]`: maximum subarray ending on `arr[i]`, but have a right to delete last element `arr[i]`.也就是你可以删，也可以不删，但你如果删必须删除最后一个, 也就是`arr[i]`. 那么状态转移方程如下
$$
\begin{align}
\rm{DP}[1][i] &= max(\rm{DP}[1][i-1] + arr[i],arr[i],\rm{DP}[0][i-1])\\

\rm{}DP[1][0] &= arr[0]
\end{align}
$$
这个理解比较费脑筋，但我来解释一下,
- `DP[1][i-1] + arr[i]`: 我删除前面的任何一个点了.
- `arr[i]` : 删掉前面全部的了,由于`DP[1][i-1]`为负数,只是累赘.
- `DP[0][i-1]`: reset前面的删除，我现在碰到负数的global min了，我要删`arr[i]`了!


## code

```python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # DP[0][i]: maximum subarray ending on arr[i].
        # DP[1][i]: maximum subarray ending on arr[i], optionally have the right to drop the arr[i].

        
        # declare DP and initialization
        DP = [[0 for _ in range(len(arr))] for _ in range(2)]
        DP[0][0] = arr[0]
        DP[1][0] = arr[0]
        

        for i in range(1,len(arr)):
            # kadane' algorithm
            DP[0][i] = max(DP[0][i-1] + arr[i], arr[i])
            # 可以舍弃arr[i]这一element 
            DP[1][i] = max(DP[1][i-1] + arr[i], arr[i], DP[0][i-1])

        return max(DP[1])
```


# Approach 2: Jerry's approach
Jerry定义的状态转移方程和我一模一样，但DP的定义和初始化有slight difference, 这个区别实际上就来自于初始化对于DP定义的影响.

DP定义需要:
- 初始条件
- 状态转移方程

这两个缺一不可，看这个例子jerry定义的DP如下:

- `DP[0][i]`: maximum subarray ending on `arr[i]`. 也就是一定不删. 状态转移方程如下:
$$
\begin{align}
\rm{}DP[0][i] &= max(DP[0][i-1] + arr[i],arr[i])\\
\rm{}DP[0][0] &= arr[0]
\end{align}
$$
这个和我的定义一样.

- `DP[1][i]`: maximum subarray ending on `arr[i]`, but must delete the last element `arr[i]`.也就是你可以删，也可以不删，但你如果删必须删除最后一个, 也就是`arr[i]`. 那么状态转移方程如下
$$
\begin{align}
\rm{DP}[1][i] &= max(\rm{DP}[1][i-1] + arr[i],arr[i],\rm{DP}[0][i-1])\\

\rm{}DP[1][0] &= 0
\end{align}
$$
可以看到equation (8) and (4)是唯一的区别，但这个initial condition直接造成了:
- 我的定义: 可以删除，可以不删除, 但如果删除一定删除`arr[i]`
- Jerry's 定义: 一定删除一个点, no matter what.
 
> Takehome is DP的定义不仅是state-transition function还和初始条件相关。

提醒了我们以后在设计DP时候，不仅仅要花时间和心思思考状态转移方程，初始状态也要花心思考虑. Jerry代码如下:

```python
# Jerry's code 
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # DP[0][i]: maximum subarray ending on arr[i].
        # DP[1][i]: maximum subarray ending on arr[i], optionally have the right to drop the arr[i].

        if len(arr) == 1: return arr[0]        

        # declare DP and initialization
        DP = [[0 for _ in range(len(arr))] for _ in range(2)]
        DP[0][0] = arr[0]
        DP[1][0] = 0
        
        max_so_far = arr[0]

        for i in range(1,len(arr)):
            # 可以舍弃arr[i]这一element 
            DP[1][i] = max(DP[1][i-1] + arr[i], arr[i], DP[0][i-1])
            DP[0][i] = max(DP[0][i-1] + arr[i], arr[i])
            max_so_far = max(max_so_far,DP[0][i],DP[1][i])

        # return max(max(DP[1]),max(DP[0]))
        return max_so_far
```

重点看jerry的initial conditions, 虽然DP[1][0]是强制删除了第一个node的情况，但是max_so_far考虑了必须是非空subarray的前提条件

```python
        DP[0][0] = arr[0]
        DP[1][0] = 0
        max_so_far = arr[0]
```