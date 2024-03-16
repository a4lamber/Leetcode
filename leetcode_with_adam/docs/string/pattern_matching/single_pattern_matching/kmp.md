# KMP

> KMP是一个高效的字符串匹配算法，它的时间复杂度是O(m+n)，其中m是pattern的长度，n是text的长度. 

KMP有两个难点，

- 如何理解`next`数组，以及如何生成`next`数组.
- 如何利用`next`数组来优化匹配过程

## KMP的应用

KMP虽然快，但很少被built-in function使用。KMP擅长的是pattern string有很多duplicate substring的工况，in real-world strings, 你在ctrl + F时，很少遇到需要KMP的工况。Plus, it requires O(n) space. 但在DNA sequencing中，这是一个很好的算法，因为DNA中有很多重复的序列, 这也是KMP最主要的应用场景之一.

!!! warning "思考题"
    如果你的pattern string为`abcde`, 你的next数组是全为0，那么你的KMP算法会退化成?

## next数组

> next数组，也叫longest prefix suffix (LPS) 数组 or 前缀数组，是基于pattern string生成的一个数组，用来帮助我们在匹配的时候，跳过一些不必要的比较. 
> 
> $\pi[i]$的定义为: 从index 0到index i的子串中，最长且相等的**从0开始的前缀**和**后缀ending in i**. 

!!! warning "前后缀定义"
    - 前缀：不包括最后一个字符的所有以**第一个字符开头**的所有字符
    - 后缀：不包括第一个字符的所有以**最后一个字符结尾**的所有字符

举个例子, 

![](./assets/kmp_1.excalidraw.png)

|substring|lps|prefix|suffix|
|-|-|-|-|
|"a"|0|||
|"ab"|0|||
|"abc"|0|||
|"abca"|1|"a"|"a"|
|"abcab"|2|"ab"|"ab"|
|"abcabf"|0|||


我们数学描述一下, for a string `s`

$$
\pi[i] =
\begin{cases} 
        0 \quad i = 0 \\
      \max_{j=0...i} \{j: s[0:j-1] = s[i-(j-1):i]\} \quad otherwise\\
   \end{cases}
$$

### Approach 1 暴力生成前缀数组 (成长期)

- 初始化一个长度为n的数组pi，全部元素初始化为0, 初始条件是pi[0] = 0.
- 从i=1开始遍历，对于每一个i，我们找到最大的j，使得`s[0:j] == s[i-j+1:i]`. 由于我们只关心最大的,所以我们可以把j从后往前traverse, 一旦找到一个j使得`s[0:j] == s[i-j+1:i]`


```python
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        for j in range(i, -1, -1):
            # right hand exclusive, so it's [i-j+1:i+1] instead of [i-j+1:i]
            # string comparison also costs O(n)
            if s[0 : j] == s[i - j + 1 : i + 1]:
                pi[i] = j
                break
    return pi
```

Traversal cost $O(n^2)$, 加上string comparison costs $O(n)$. The total time complexity is $O(n^3)$.

### Approach 2 优化生成前缀数组 (成熟期)

Inner iterator `j` 不需要是遍历`n`，我们可以缩小范围为遍历`pi[i-1]+1`. 这一点，利用的性质是

- `max(pi[i] - pi[i-1]) == 1`, pi数组中下一个element如果增加，至多增加1.
- 上一个数组的最长前缀长度`pi[i-1]`是我们的candidate char.
 
Starting from `j = pi[i-1]+1`. 然后我们一直往前比，直到找到一个相等的前后缀，或者j=0.

```python
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        for j in range(pi[i - 1] + 1, -1, -1):
            if s[0 : j] == s[i - j + 1 : i + 1]:
                pi[i] = j
                break
    return pi
```

但这也算minor improvement, time complexity is $O(n^2)$, 有兴趣看推导的，辗转到[OI wiki](https://oi-wiki.org/string/kmp/).

### Approach 3 究极体

接着Approach 2中当decrement by 1, 我们能否让它decrement by more呢? 

换句话说，我们遇到一个新的`i`, 直接比较`s[i] != s[pi[i-1]]`，

- `s[i]`: 新的嗷嗷待哺的character.
- `s[pi[i-1]]`: 上一个iterator `i-1`所结尾的数组的最长前缀长度. 由于0-indexed, 所以这个正好就是我们要比较的potential char.

Dry run见下图

![](./assets/kmp_2.excalidraw.png)


```python
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        # j 从前一个pi[i-1]的值开始遍历
        j = pi[i - 1]
        
        # 如果下一个不同，我继续往前backtrack, 不同于approach 2的decrement by 1, 我们是跳跃着减少, 最后收敛于pi[0] == 0
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        # 跳出循环后两种情况:
        # 1. j == 0, 说明没有找到相同的前后缀, do nothing
        # 2. s[i] == s[j], 说明找到相同的前后缀, 找到increment by 1
        if s[i] == s[j]:
            j += 1
            pi[i] = j
        else:
            pi[i] = j
    return pi
```

好了，现在讲完了前缀函数next的前世今生，我们来讲一下前缀函数的应用


## 前缀函数的应用

### 1. KMP找子串

给你一个主串T和一个模式串p，你要在T中找到p第一次出现的index。如果找不到，返回-1。

```python
# KMP 匹配算法，T 为文本串，p 为模式串
def kmp(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    # 生成前缀数组
    pi = generate_lps(p)                      
    
    # j 为模式串中当前匹配的位置, i 为文本串中当前匹配的位置, i从不回退, j会根据next数组回退
    j = 0
    for i in range(n):
        # 如果模式串前缀匹配不成功, 将模式串进行回退, j == 0 时停止回退
        while j > 0 and T[i] != p[j]:
            j = pi[j - 1]
        # 当前模式串前缀匹配成功，令 j += 1，继续匹配
        if T[i] == p[j]:
            j += 1
        # 当前模式串完全匹配成功，走到模式串的tail了, return 匹配的起始index
        if j == m:
            return i - j + 1
    # 匹配失败，返回 -1
    return -1
```





## 相关题目

- 26 implement strstr and solution here

## Reference

- [Abdul,适合理解KMP concept](https://www.youtube.com/watch?v=V5-7GzOfADQ&ab_channel=AbdulBari)
- [KMP by Neetcode, 看前15分钟即可，这时候思路还不清晰](https://www.youtube.com/watch?v=JoF0Z7nVSrA&ab_channel=NeetCode)
- [lijingran's blog讲的很简洁](https://www.cnblogs.com/lijingran/p/8619711.html)
- [LC CHN 理解next数组是怎么生成的](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/1119642/duo-tu-yu-jing-xiang-jie-kmp-suan-fa-by-w3c9c/)