---
tags:
    - Two Pointers
    - String
    - Greedy
---
# 680 Valid Palindrome II

是[125 valid palindrome](https://leetcode.com/problems/valid-palindrome/description/)的扩展, 作为双指针入门是很不错的一题.

## Approach 1 Two Pointers

一共有三种情况:

- 不需要删除任何字符,就是palindrome
- 在two pointer两端朝中间travel的过程中,
    - 左边`i`遇到不一样的字符, 判断`i+1`到`j`是否是palindrome
    - 右边`j`遇到不一样的字符，判断`i`到`j-1`是否是palindrome

可以看出，我们需要执行is_palindrome三次，所以构建一个helper function来判断是否是palindrome.

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(word,left,right):
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        i,j = 0,len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        # we remove 0 char
        if i >= j:
            return True
        if is_palindrome(s,i+1,j) or is_palindrome(s,i,j-1):
            return True
        
        return False
```