---
tags:
    - Bit Manipulation
    - Recursion
    - Math
---
# [231 Power of Two](https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19)


这题三种解法，重点掌握bit manipulation的

- loop
- recursion
- bit manipulation

## Approach 1 loop

判断对于一个integer `n`, 是否存在另一个interger `x` 使得 $2^x = n$，那么你的solution就只能是,

$$
2^x \quad x\in \mathbb{N*0} 
$$
where $\mathbb{N}^{*}$ is 正整数.

!!! tip tip
    注意，在计算机和集合论中，$\mathbb{N}$ 定义为包括0的正整数. 但在数论中，$\mathbb{N}$ 定义为不包括0的正整数. 所以在这里做了区分。Conventionally, $\mathbb{N_0}$ is used to denote the set of non-negative integers, $\mathbb{N}^{*}$ for positive integers. 如果你想严谨一些的话.

既然结果肯定是, `{1, 2, 4, 8, 16...}`, 我的思路是设计一个从0不断乘以2的循环，直到找到一个数等于n，或者超过n.

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        counter = 0
        bar = 2**counter
        
        while bar <= n:
            if bar == n:
                return True
            counter += 1
            bar = 2**counter
            
        return False
```

## Follow-up: w/o loop/recursion

能否不用loop或者recursion来求呢? 对于2的幂次方，有一个快速判断的trick, 也就是`&` operator的性质, 先看如下表

|$2^x$|in binary|$2^x - 1$|in binary|
|---|---|---|-|
|$2^0 = 1$|0001|$2^0 -1 = 0$ |0000|
|$2^1 = 2$|0010|$2^1 -1 = 1$ |0001|
|$2^2 = 4$|0100|$2^2 -1 = 3$ |0011|
|$2^3 = 8$|1000|$2^3 -1 = 7$ |0111|
|$2^4 = 16$|10000|$2^4 -1 = 15$ |01111|
|$2^5 = 32$|100000|$2^5 -1 = 31$ |011111|

我们随便取俩做个计算, 比如`2=0010` and `1=0001`
```
    0010
  & 0001
    ------
    0000
```

对于一个power of two的数，它的二进制表示中只有一个1，所有其他位都是0. 所以它减去1的话，就是lower bits都是1. 所以它们的`&`操作结果就是0.


```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        1:          0:
        01          00
        2:          1:
        10          01
        4:          3:
        100         011
        8:          7:
        1000        0111
        16          15:
        10000       01111

        so for n = 2^x, we always have the properties that n & (n-1) == 0
        """
        if n <= 0: return 0
        return n & (n-1) == 0
```
