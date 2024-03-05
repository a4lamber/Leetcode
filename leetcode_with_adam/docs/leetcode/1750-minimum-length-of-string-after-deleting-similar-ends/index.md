---
tags:
    - Two Pointers
    - String
---
# [1750 Minumum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05)


## Approach 1: Two Pointers

If you understand what the question is asking, you are half way there. The string `s` consists only of `a`, `b` and `c`. You can perform the following operations,

- delete a non-empty prefix of `s` with the same characters 
- delete a non-empty suffix of `s` with the same characters. But the characters you are deleting must be the same as the prefix.
- the prefix and suffix don't intersect

In this case, we having following scenarios, 

```
# 1. with only 1 char left in the middle
"aba" --> "b"

# 2. with more than 2 char left in the middle but cancelable
"aabbaa" --> "bb" --> ""

# 3. with more than 2 char left in the middle but not cancelable
"aabcaa" --> "bc"
```

Also we could have edge case like `s = "c"`. Based on those information, i have came up with the following solution,


```python
class Solution:
    def minimumLength(self, s: str) -> int:
        # edge case
        if len(s) == 1:
            return 1

        # O(n) or O(nlogn) at worst
        left,right = 0,len(s)-1

        while left < right:
            # if not the same, we quit
            if s[left] != s[right]:
                break
            # base case like "cbc"
            if right - left == 2:
                return 1

            # if we get here, 1st and last char will be the same
            curr = s[left]
            while curr == s[left] and right > left:
                left += 1

            while curr == s[right] and right > left:
                right -= 1

        if left == right:        
            # empty the whole string
            return 0
        else:
            # have some substring left
            return right - left + 1
```

But now i look at it, i found out there are many edge cases and boundary shenanigans to work with. We can create a much generalized solution according to editorial solution,


```python
class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        # Delete similar ends until the ends differ or they meet in the middle
        while left < right and s[left] == s[right]:
            curr = s[left]

            # Delete consecutive occurrences of c from prefix
            while left <= right and s[left] == curr:
                left += 1

            # Delete consecutive occurrences of c from suffix
            while right > left and s[right] == curr:
                right -= 1

        # Return the number of remaining characters
        return right - left + 1
```


|s|comment|analysis|
|-|-|-|
|`"c"`|pass|it doesn't get into the while loop|
|`"aba"`|pass|left points to `b`, right points to `b` as well|
|`"aabbaa"`|pass|left points to the `a` in `bba`, right points to `b` in the middle `bba`. In this case, `left` always go past `right` by 1|
|`"aabcaa"`|pass|left points to `b` and right points to `c`. This is the most general case since it expands to every `aabxxxxxxcaa` cases|


比较难的一点是，怎么在interview setting相处这么漂亮的边界处理方式. 特别是left=right+1 (left走到right右边了)的边界跳出格式, 把两个case统一了. 其实这和binary search的边界条件那里很像，搞明白什么条件跳出.


