---
tags:
    - Math
    - Prefix Sum
---

# [2485 Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13)

Brute force为linear scan, 然后暴力求和, O(n^2). 但是这题有一个trick, 就是可以用prefix sum来优化.

## Approach 1 Prefix Sum

这题的pivot integer, 就是找到一个index $x$, 使得这个index左边的和等于右边的和. 满足的条件是 
$$
\begin{equation}
1 + 2 + 3 + ... + x = x + (x+1) + (x+2) + ... + n
\end{equation}
$$
是一个both ends inclusive的range sum. `[i...x] == [x .. n]`, 在linear scan时候，可以maintain两个变量

- prefix_sum: 从1到i的和
- suffix_sum: 从i到n的和

每次更新时, prefix_sum加上当前index, suffix_sum由于需要保持inclusive, suffix_sum的更新需要减去previous index. 如果两者相等, 则返回当前index.

```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        # 1 + 2 ... + x == x + (x+1) + ... + n
        # at most 1 pivot index, else return -1
        
        prefix = 0
        suffix = (1 + n)*n//2
        
        for i in range(1,n+1):
            prefix += i
            suffix -= (i-1)
            if prefix == suffix:
                return i
                
        return -1
```