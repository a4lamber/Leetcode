---
tags:
    - String
    - Stack
---

# [1544 Make The String Great](https://leetcode.com/problems/make-the-string-great/description/?envType=daily-question&envId=2024-04-05)


## Approach 1 Stack

```python
class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        def is_bad(a,b):
            if a != b and (a.upper() == b or a == b.upper()):
                return True
            return False
        
        # Iterate over 's'.
        for curr_char in list(s):
            # If the current character make a pair with the last character in the stack,

            if stack and is_bad(curr_char,stack[-1]):
                stack.pop()
            else:
                stack.append(curr_char)
        
        # Returns the string concatenated by all characters left in the stack.
        return "".join(stack)
```

You can improve the code by comparing if the unicode difference between the two characters is 32. This is because the difference between the uppercase and lowercase characters is 32. 

!!! tip
    You can use the `ord()` function to get the unicode of a character. As for quickly compare whether two character are upper-lower-conjugate, you can use `abs(ord(a) - ord(b)) == 32`.


```python
class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        # Iterate over 's'.
        for curr_char in list(s):
            # If the current character make a pair with the last character in the stack,
            # remove both of them. Otherwise, we add the current character to stack.
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        
        # Returns the string concatenated by all characters left in the stack.
        return "".join(stack)
```



