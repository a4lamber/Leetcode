---
tags:
    - String
    - Stack
---

# [1614 Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04)

intuition: 

- 这道题目是一个括号匹配的题目，我们需要找到最大的括号嵌套深度. 一看到括号就想到stack和valid parentheses这一类题目.

## Approach 1: Stack

由于每一个opening parantheses都会有一个closing parantheses, 所以我们可以用stack的来记录当前的括号深度，没遇到一个opening parantheses, 我们就把深度加1, 遇到一个closing parantheses, 我们就把深度减1。

有两个edge case需要考虑:

- "()" == 1
- "1" == 0


```python
class Solution:
    def maxDepth(self, s: str) -> int:
        """
        () == 1
        """
        stack = []
        res = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
            
            res = max(res,len(stack))
        
        return res
```