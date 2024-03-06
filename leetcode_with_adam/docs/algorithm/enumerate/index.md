# Enumerate (枚举)


## Enumerate定义

> An `enumeration` is a complete, ordered listing of all the items in a collection. The term is commonly used in mathematics and computer science to refer to a listing of all of the elements of a set. In the context of DSA, it refers to try out all potential solutions to a problem.


!!! tip
    答题顺序第一步就是先想出brute force(enumerate), 之后再扩展其它算法的可能性。结合constraint给的范围，来排除掉一些在当前constraints下，复杂度太高的备选算法，然后再从剩下的算法中选择最优或你会的。


## Enumerate的应用

- 暴力搜索你的password啊, 这些都是枚举. 比如你的密码在8-16位，通过你定义的password需求，大小写等，排除掉一些不可能的组合，然后再去尝试剩下的组合。

比较关键的是:

## 例题

枚举三要素

- `define solution space`: 定义解空间, 即然要暴力搜索，要想清楚可能的情况是什么？要枚举什么？
- `shorten solution space`: 缩小解空间, 通过constraints来缩小解空间，是否有血情况不需要考虑？比如上面的密码例子，你不需要考虑全是小写的情况，因为密码规范要求必须有大写。通过大小写，长度, 特殊符号等等种种来缩小解空间, 提高效率。
- `order of enumeration`: 枚举的顺序, 有时候枚举的顺序也是有讲究的。循环时，i, j还是i+1, j+1, 边界点啊，先循环i or j

!!! 例题
    一个数组中的数，互不相同，求其中和为0的数对的组合

### 方法1: 枚举所有情况

```python
for i in range(n):
    for j in range(n):
        if i != j and a[i] + a[j] == 0:
            res += 1
```

这个方法实际上枚举了$n^2$次. 但我们有两个小优化可以做，

- 我们并没有充分利用`一个数组中互不相同`这个条件。我们只是考虑到了情况，通过`i != j`来排除掉了重复的情况。但是我们可以通过`i > j`来排除掉一些情况，这样可以减少$n$次枚举次数, 也就是$O(n^2-n)$
- 题目没要求是有序还是无序的。A.K.A. 如果(a,b)是答案，那么(b,a)也是答案。所以我们可以通过`i < j`来考虑第一个数字在前的情况，这样可以减少$n/2$次枚举次数, 最后再答案x2即可。也就是$O(\frac{n^2}{2})$


## 方法2: 优化枚举

```python
for i in range(n):
    for j in range(i):
        if a[i] + a[j] == 0:
            res += 1
res *= 2
```
你把所有(i,j)列下, 会发现这样的组合是不会重复的。因为`i > j`, 所以不会有重复的组合。这样我们就减少了一半的枚举次数。

```
(1, 0)
(2, 0)
(2, 1)
(3, 0)
(3, 1)
(3, 2)
(4, 0)
(4, 1)
(4, 2)
(4, 3)
```

同理你也可以反一反，让`i < j`

```python
for i in range(n):
    for j in range(i+1, n):
        if a[i] + a[j] == 0:
            res += 1
res *= 2
```

列出所有结果
```
(0, 1)
(0, 2)
(0, 3)
(0, 4)
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```

结合以上两种情况，这种算法的复杂度，$O(\frac{n^2}{2})\approx O(n^2)$, 虽然没有大的进化，但是我们通过枚举的优化，减少了一半的枚举次数。

## 方法3: 利用辅助空间

这一段略，要么用array结合bucket sort的思想，要么hashmap.


## 相关题目

- [1 two sum](https://leetcode.com/problems/two-sum/description/)
    - 梦开始的地方，这题的暴力解法就是枚举所有情况，然后找到答案. 你可以试试方法2里的优化枚举.

## Reference

- [enumerate in cybersecurity](https://medium.com/@zapbroob9/what-is-enumeration-in-cybersecurity-f3391ef533c0)