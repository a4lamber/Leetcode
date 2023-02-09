
# Approach 1 bit manipulation
<!-- Describe your approach to solving the problem. -->

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
利用exclusive or的特性, 如果

$$
\begin{align}
LHS &= a \bigoplus b \bigoplus c \bigoplus a \bigoplus c \\
&= \left(a \bigoplus a\right) \bigoplus b \bigoplus \left(c \bigoplus c\right)\\
&= b
\end{align}
$$
where $\bigoplus$ is exclusive or, it has commutative property (交换律)

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






# Complexity
- Time complexity: $O(n)$ one-pass solution
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a^num

        return a
```