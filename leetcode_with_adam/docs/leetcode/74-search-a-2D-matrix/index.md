---
tags:
    - Array
    - Binary Search
    - Matrix
---

# [74 Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

归化的想法，转移成已知的问题。如果给定的不是二维数组，而是1d array, 就很简单。那么for a matrix (m x n), 我们可以有一个1D array of size m*n, 也就是`nums[0..m*n-1]`. 我们只要在这个1d 数组里面做binary search就可以了. 但我们有的却是一个2d array, 实际上我们只要找到这个关系即可, `num[z] == matrix[x][y]`, 我们可以建立一个映射关系，

$$
\begin{equation}
    f(z) = (x,y) = (\left\lfloor \frac{z}{n}\right\rfloor, z\bmod n)
\end{equation}
$$
where $m$ and $n$ are the number of rows and columns of the matrix, respectively.


!!! note "复杂度"

    - 时间复杂度：$O(\log(mn)) = \log(m) + \log(n)$.
    - 空间复杂度：$O(1)$.


```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # problem: 
        #   1. find the target;
        #.  2. wrap around the rows somehow.

        # Solution:
        # BFS: linear search or flatten it to a 1D row and do your normal binary search. O(mn)
        # m,n for row and col, respetively.
        # i = 0 .. m*n-1
        # i --> matrix[i//n][i%n]
        
        m,n = len(matrix),len(matrix[0])        
        left,right = 0,m*n-1

        while left <= right:
            mid = (left + right)//2
            x,y = mid//n, mid%n
            curr = matrix[x][y]
            if  curr == target:
                return True
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
```