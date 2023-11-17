---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Readme

这一题输入为integer `numRows` and 输出为一个nested数组`[[1],[1,1],....]`，输出的数组中，包含着一个个小数组，每个小数组都包含了三角形每一行中的信息.

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)


杨辉三角形, dynamic programming的入门级题目，这一题思路用dp framework 非常简单:
- `base cases`: current state information不依赖于previous layers
- `recurrence cases`: 也就是current state的数据依赖于previous layers

题目的constraints为 
$$
1\leq n\leq 30
$$

这样的话我们把前几列列一下就清晰了
```
n = 1 --> [[1]] // base cases
n = 2 --> [[1],[1,1]] // base cases
n = 3 --> [[1],[1,2,1]] // recurrence cases
n = 4 --> [[1],[1,2,1],[1,3,3,1]] // recurrence cases
n = 5 --> [[1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] // recurrence cases
```

## Code


```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 杨辉三角形 binomial coeffient 类型;

        # edge cases
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]

        # recurrence cases
        triangle = [[1],[1,1]]
        # starting from row 3
        for i in range(3,numRows+1): # +1 是因为right hand exclusive in python
            # initialze the array of size 
            row = [None] * i # 每一行都有rownumber数量的elements
            
            # add the 1st element
            row[0] = 1
            for j in range(1,i-1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            
            # add the last element
            row[i-1] = 1

            # append to the result list
            triangle.append(row)  

        return triangle
```

