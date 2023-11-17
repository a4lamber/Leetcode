---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---
# Approach 1: Horizontal scanning
<!-- Describe your approach to solving the problem. -->

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
假设有一个list里面有很多不同的strings, 要找出其中的common pre-fix, 我们设计一个函数$P(0,1,2,\dots,n-1)$ 其中 0, 1, 2,$\dots$为其中所有的string的index, 我们的目标是找到:
$$
P(0,1,\dots,n-1)
$$
可以将这个问题转化为
$$
P(0,1,\dots,n-1) = P(\dots P(P(P(0,1),2),3)\dots,n-1)
$$


## Algorithm

- create a function `twoStrCommonPrefix()` that takes input of two strings and output the common prefix between the two, AKA 负责$P(1,2)$
- traverse the whole list `strs` and call the function `twoStrCommonPrefix` n -1次, valla 

## Complexity
- Time complexity: $O(S)$ where S is the total number of chars inside the list `strs` 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
class Solution:
    def twoStrCommonPrefix(self,s,t):
        # s: input string 1
        # t: input string 2
        # res [str]: common prefix between two strings
        res = ""

        # determine the min length between two characters
        min_length = min(len(s),len(t))

        # iterate the smaller string
        for i in range(min_length):
            # 判断俩字符是否相等
            if s[i] == t[i]:
                # 相等则累加入res
                res += s[i]
            else:
                # 不相等直接return res为common prefix 
                return res
        
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # horizontal scanning appraoch

        # edge cases
        if len(strs) == 0:
            return ""


        res = strs[0]
        for i in range(len(strs)-1):
            # 比较俩相邻的string
            res = self.twoStrCommonPrefix(res,strs[i+1])

        
        return res


```

# Approach 2: Vertical scanning
<!-- Describe your approach to solving the problem. -->


## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

## Complexity
Vertical scanning在算法复杂度上，并没有什么优化, 但实际performance有很大的提升, 由于horizontal scanning永远是worst case scenerio (traverse all the strings inside the list), 而horizontal scanning并不一定总是worst case.

- Time complexity: $O(S)$ where S is the total number of chars inside the list `strs` 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan Solution
        
        # if no common prefix, then ""
        res = ""

        # iterate i time where i equals number of chars in the str
        # i 为比较第几个character
        for i in range(len(strs[0])):
            # traverse str
            for str in strs:
                # 判断是否index out of range OR 不相等
                if i == len(str) or str[i] != strs[0][i]:
                    return res
            
            # 累加入string
            res += strs[0][i]

        return res
```