---
tags:
    - String
---

# [6 ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/description/)

这题只能算脑筋急转弯，不怎么考数据结构。我的思路是

- 创建matrix
- 设计一个flag，用来判断是向上还是向下, 触底反弹和触顶反弹
- 把值填进matrix
- 最后把matrix转换成string

我只过了少数test case, 其它有index error, 说明在边界处理上不干净. 除此之外还有几个缺陷:

- matrix的大小不好确定, 且最后flatten比较expensive

## Approach 1
把每一行浓缩成一个string,

```python
s = "paypalishiring"
rows = [
    "pahn",
    "aplsiig",
    "yir"
]
```

设计一个`upward` flag, 用来判断是向上还是向下, 触底反弹和触顶反弹

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # construct a 2D array
        # convert the array to a string
        # worst case
        if numRows == 1:
            return s
        
        # 把每一行浓缩成一个string了
        rows = [""] * numRows
        upward = True
        curr_row = 0

        for char in s:
            rows[curr_row] += char
            # switch direction
            if curr_row == 0 or curr_row == numRows - 1:
                backward = not backward
            
            if backward:
                curr_row -= 1
            else:
                curr_row += 1
        return "".join(rows)
```
