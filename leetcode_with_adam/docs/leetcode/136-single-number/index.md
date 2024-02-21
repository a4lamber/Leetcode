---
tags:
  - 1
---

# [136 Single Number](https://leetcode.com/problems/single-number/description/)


## Approach 1 bit manipulation
<!-- Describe your approach to solving the problem. -->

XOR has two properties:

- `a^a = 0`
- `a^0 = a`


举个例子

$$
\begin{align}
LHS &= a \oplus b \oplus c \oplus a \oplus c \\
&= \left(a \oplus a\right) \oplus b \oplus \left(c \oplus c\right)\\
&= 0 \oplus b \oplus 0\\
&= b
\end{align}
$$
where $\oplus$ is XOR, XOR has commutative property (交换律)

这个方法可以很方便的找到unique value, 再举个例子，一个数列`he = [2,2,3,1,3]`, convert it to binary and do the following

$$
\begin{align*}
    10\\
    10\\
    11\\
    01\\
    11\\
    ----\\
    01
\end{align*}
$$
两两直接进行exclusive or, solution in binary is `01` convert back, it's 1



!!! Complexity
    Time complexity $O(n)$, one-pass solution
    Space complexity $O(1)$


# Code
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a^num

        return a
```