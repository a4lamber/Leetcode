---
tags:
    - String
    - Dynamic Programming
    - Stack
---

# [678 Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2024-04-07)

先来理解一下这题，observations如下:

- 一共只有三种字符: `(`, `)` and `*`
- 赖子牌，`*` 可以代表三种以上`(` or `)` or empty string `''` 
- 那么对于每一个`*`都有三种可能性，那么总共有$3^{*}$种可能性

先把可能性的path画出来,

这种暴力的树一画出来，会发现有很多重复的子问题，所以暗示我们可以用DP来解决这个问题.

## Approach 1 Top-down with memoization

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        observation:
        - 只有(,) and *
        - 和麻将牌的赖子一样，*能代表任何( or ) or empty string
        - parathesis questions must involve stack to push '(' in when necessary
        - 假设我们有x个*, 那么就有3^{*}个可能性
        """
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        return self.is_valid_string(0,0,s,memo)
    
    def is_valid_string(self,index,open_count,s,memo):
        # base case
        if index == len(s):
            # reach the end of the string,
            return open_count == 0
        
        # in-memo
        if memo[index][open_count] != -1:
            return memo[index][open_count] == 1
        
        is_valid = False
        if s[index] == '*':
            # '*' as '('
            is_valid |= self.is_valid_string(index+1,open_count+1,s,memo)
            if open_count > 0:
                # '*' as '('
                is_valid |= self.is_valid_string(index+1,open_count-1,s,memo)
            # treat as empty string
            is_valid |= self.is_valid_string(index+1,open_count,s,memo)
        else:
            if s[index] == '(':
                is_valid = self.is_valid_string(index+1,open_count+1,s,memo)
            elif open_count > 0:
                is_valid = self.is_valid_string(index+1,open_count-1,s,memo)
        
        # mark it True or False
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid
```