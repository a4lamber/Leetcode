# Brute Force

> Brute Force: 暴力匹配, 也叫朴素匹配算法 (naive string matching), 是一种简单直接的字符串匹配算法. 该算法的基本思想是: 从主串$T$的第一个字符开始, 依次比较主串$T$和模式串$P$的字符, 如果相等, 继续比较下一个字符, 如果不相等, 主串$T$的指针后退一位, 模式串$P的指针归零, 重新开始匹配. 这种算法的时间复杂度是O(m*n), 其中m和n分别是主串和模式串的长度. 由于该算法的效率较低, 因此在实际应用中很少使用.

## 思路

1. 计算模式串的长度$m$和主串的长度$n$, 用两个指针$i$和$j$分别指向主串和模式串的第一个字符.
2. 同时traverse主串和模式串, $T[i]$ and $P[j]$
      1. 如果相等，advance both pointers直到走到模式串的末尾
      2. 如果不相等，则reset i's pointer 到应该匹配的下一个位置，reset j's pointer 到模式串的开头
3. 如果主串或者模式串走到了末尾，则返回匹配的起始位置

## 代码实现

```python
def brute_force(T,P):
    n,m = len(T), len(P)
    i,j = 0,0
    while i < n and j < m:
        if T[i] == P[j]:
            i += 1
            j += 1
        else:
            # not matching, reset to i-j, move to next by increment 1
            i = i - j + 1
            j = 0
    
    # 到这里有两种情况
    # 1. j == m, 说明找到了匹配的模式串, 等价于exhaust all pattern string
    # 2. 其它任何情况都是没找到
    if j == m:
        return i - j
    else:
        return -1
```

## 复杂度分析

Time complexity是$O(m*n)$, 其中$m$和$n$分别是主串和模式串的长度，不是很高效的算法，有重复计算的风险. Worst case是

```
T = 'aaaaaaaaaa'
P = 'aaaf'
```

可以看到，我们每一次匹配，都会比较到最后一次，然后才会发现不匹配，然后重置i和j的指针. 但我们明明知道，如果前面的字符都是a，那么我们可以直接跳到最后一个a的位置，而不需要一个一个的比较. 这就是Brute Force的缺点，重复计算, 这就是我们可以优化的空间所在。
