---
draft: true
date: 2023-01-27
authors:
  - adam
description: >
    two sum, where the dream begins
categories:
  - hash
  - easy
---

# 1 two sum

> LeetCode算法submit时，会给一个比较大的算例，来算runtime和memory consumption，主要是用来区分好的算法和差的算法

## Brute force
这一题我下意识的解法是, traverse这个list twice with nested loop, 然后根据题目做两个if判断:
- 两个element之和等于本身
- 不能用同样的element twice
之后只需要break out the nested loop就可以了, 代码如下

```python
"""
brute force intuition
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define return list
        result = []
        # define flag variable to breakout nested loop
        break_out_flag = False
        for i, item_x in enumerate(nums):
            for j, item_y in enumerate(nums):
                # check for two conditions
                # 1. sum of two variables equals to target
                # 2. make sure it's not same elements
                if item_x + item_y == target and i != j:
                    result.append(i)
                    result.append(j)

                    # added a flag variable to break out nested loop
                    break_out_flag = True
                    break
            if break_out_flag:
                break

        return result
```
这一题的时间复杂度是$O(n^2)$, 因为`nums`的size是n， 然后nested loop比较了所有的情况，也就是$n \times n$.


> $O(n^2)$: quadratic, every element in a collection needs to be compared to every other element.



在jerry的提示下，这种brute force的解法可以进行一次小优化，nested loop中，假设第一圈需要比较n次，那么第二圈只需要比较n-1，直到最后一圈为1, 如下图:

```
假设nums = [1, 2, 3, 4, 5, 6], target = 8

1+2, 1+3, 1+4, 1+5, 1+6
2+3, 2+4, 2+5, 2+6
3+4, 3+5, 3+6
4+5, 4+6
5+6
```
时间复杂度的计算，也就是等差数列求和
$$
\begin{align}
S_n &= (a_1 + a_n)\frac{n}{2}\\
    &= a_1n + \frac{n(n-1)d}{2}
\end{align}
$$
where d is 公差.
所以你计算一下时间复杂度还是$O(n^2)$, 具体实现如下
```python
"""
改进版brute force
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define return list
        result = []
        # define flag variable to breakout nested loop
        break_out_flag = False

        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break_out_flag = True
                    break
            if break_out_flag:
                break
    
        return result
```

## Two-pass Hash table

题干: 在一个array中，找到两个element, 满足这两个element之和等于target value, 然后输出这两个element的index, 且这两个element必须是不同的element;

由于brute force解法是traverse on array with nested loop, 一次traverse list的复杂读是$O(n)$, nested则$O(n^2)$. 

思路就是换一个data structure, 提高效率, 那首先可以将题干转化为一个需要满足的条件, 条件如下:

> 在一个数据结构中，是否存在不相同的两个element, 满足这两个element之和为target, 而不考虑collision的情况，以空间换时间，可以选择hash来解决这个问题. 

这个解法叫**two-pass hash table** 也就是traverse twice
- 第一个traverse, 建立一个hash table;
- 第二个traverse, 找里面是否存在符合条件的element;


具体实现方法如下:

```python
"""
two-pass hash table
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare a hashmap
        hashmap = {}
        # initialize the hashmap with key-value pair
        """
        Example:
        nums = [5,1,9,10]
        saves in the form of {value:index}
        hashmap = {
            5: 0,
            1:1,
            9:2,
            10:3
        }
        """
        for i in range(len(nums)):
            # value to be key, index be value
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            # calculate the condtion needs to be met
            condition = target - nums[i]
            # check both conditions
            # check 为了met condition的条件是否存在于hash中，以及hash是否等于其本身
            if condition in hashmap and hashmap[condition] != i:
                return [i,hashmap[condition]]


```

关于复杂度
- 时间复杂度: we traverse twice, so the overall time complexity $O(n)$ 
- 空间复杂度: 需要存一下hash, 那么需要$O(n)$的空间复杂度




## One-pass Hash Table
回想一下上一个解法, two-pass hash table:
- initialize a hashtable (traverse once)
- look for condition (traverse)

这两步合并为一步，就是one-pass hash table, 现在我们可以在initialize的过程中将两个合在一起, 变为:
- 边initialize 边look for condition  


```python
"""
one-pass hash table
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare a hashmap
        hashmap = {}
        # initialize the hashmap with key-value pair
        """
        Example:
        nums = [5,1,9,10]
        saves in the form of {value:index}
        hashmap = {
            5: 0,
            1:1,
            9:2,
            10:3
        }
        """
        for i in range(len(nums)):
            # calculate the condition needs to be met
            condition = target - nums[i]
            # check whether the condtion has been met yet
            if condition in hashmap:
                return [i, hashmap[condition]]
            # initialize 
            hashmap[nums[i]] = i



```


## 算法比较

|Solution|时间复杂度|空间复杂度|-|-|
|-|-|-|-|-|
|-|-|-|-|-|
