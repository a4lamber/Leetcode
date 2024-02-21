# Bit Tricks for CP

这一章我们来看一些bit manipulation的tricks, 这些tricks可以帮助我们快速的解决一些问题，要注意的是以下这些trick, 就像等价数列的求和公式一样，作为一个数学工具让我们加速做一些计算, 对于某些需要recursion或者loop的题目，我们假设知道这些tricks, 就可以不用error-prone的recursion或者loop来解决问题. 但这一部分知识的学习纯粹只是为了解puzzle,因为:

- 牺牲了readability
- 有些trick可能会导致overflow. handle overflow的问题
- 并不涉及到什么数据结构，只是用来做
    - 局部优化 (CP中偶尔需要)
    - 某些tricks不需要recursion or loop.

算是比较low priority的知识点.

## 1. 奇偶性

通常判断odd or even会用到modulus operator, 比如

```python
if x%2 == 0:
    print("Even")
else:
    print("Odd")
```

但我们可以看least significant bit(最右边的bit), 是否是0 or 1来判断奇偶性。如果是0, 那么是even, 如果是1, 那么是odd. 这也是为啥叫二进制的原因，因为奇数还没进位呢. 我们dry run一下`7=111`, 
```
    111
   &  1
   -----
      1
```
所以以后我们可以用下面的lambda function来判断奇偶性, 

```python
is_odd = lambda x: x&1 == 1
```


??? note "[Leetcode 191 Number of Bits](https://leetcode.com/problems/number-of-1-bits/description/)"
    Given an unsigned integer, calculate the number of '1' bits it has (also known as the Hamming weight). For example, the 32-bit integer `11` has binary representation `00000000000000000000000000001011`, so the function should return `3`. 
    
    Solution [here](../../leetcode/191-number-of-1-bits/index.md).




## 2. Power of Two

检验一个integer `n`是否是一个power of 2, $n=2^x$, 我们只需要做,

```python
# edge case for this operation
if n == 0:
    return True

if n & (n-1) == 0:
    return True

return False
```

??? note "[Leetcode 231 Power of Two](https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19)"
    Given an integer `n`, write a function to determine if it is a power of two. Let's say `n=16`, then `16=2**4`, so it's a power of 2.

    Solution [here](../../leetcode/231-power-of-two/index.md)


## 3. Play with kth Bits

这个trick定义的kth bits from the right (kth least significant bit), 有以下四种操作, 假设我们有一个数字`n`,

|-|-|
|-|-|
|check if $k_{th}$ bit is set|`n & (1 << k) != 0`|
|toggle $k_{th}$ bit|`n ^ (1 << k)`|
|set $k_{th}$ bit|`n | (1 << k)`|
|unset $k_{th}$ bit|`n & ~(1 << k)`|

### 3.1 check if $k_{th}$ bit is set

把`1`向左移动`k`位 (`1<<k`)，然后和`n`做`&`操作，如果结果不是0，那么`kth` bit是set.

### 3.2 Toggle $k_{th}$ bit

同理，把`1`向左移动`k`位 (`1<<k`)，然后和`n`做`^`操作，就是toggle了`kth` bit. 由于是XOR, 就两种case:

- kth bit is 0, then 0 ^ 1 = 1
- kth bit is 1, then 1 ^ 1 = 0

### 3.3 Set $k_{th}$ bit

这个同理，很好理解

### 3.4 Unset $k_{th}$ bit

很好理解.


## 4. Multiply or Divide a number by $2^k$

|operation|-|example|
|-|-|-|
|Multiply by $2^k$|`n << k`|-|
|Divide by $2^k$|`n >> k`|-|

!!! warning warning
    往左是乘法，往右是除法. 但是要注意，如果是right shift for negative number 以及overflow的问题.


## 5. Find if $n \% 2^k$

一个用bitwise快速计算, 任意数字`n` mod $2^k$的方法是,

$$
x \& ( (1<<k) - 1)
$$

我们来举个例子`n=10, k=2`,
```
10 % 2^2 = 2
```


## 6.

Place holder here. Come back in the future.




## Reference

- [TLE by Priyansh, 10 bitwise tricks](https://www.youtube.com/watch?v=LGrE0siZ-ZA&ab_channel=TLEEliminators-byPriyansh)