# Approach 1: brute force

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
对于任何valid string来说，都会存在至少一对bracket pair, 当你移除这一对bracket pair时，你会发现，至少还会存在一对bracket pair, 直到string长度为0。bracket pair的定义是 `"{}"` or `"()"` or `"[]"`. 

test cases有几种类型:
- nested: `"{([])}"`
- side-by-side: `[](){}`


## Approach
<!-- Describe your approach to solving the problem. -->
之前在codewar做过这道题，最后看到的解法就是这个，非常elegant.



## Complexity
- Time complexity: $O(n^2)$, `s.replace` is O(n), for every pair of bracket.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python
"""
brute force solution, i have done it once on code war,

time complexity: O(n^2), 假设我们的string s长度为n，
作为一个valid parathenes, 里面有n/2 pair of bracket, 
我们需要traverse至少 n/2遍 of length n, 所以时间复杂度为n^2

space complexity: O(1)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = "()"
        curlyBracket = "{}"
        squareBracket = "[]"

        while parentheses in s or curlyBracket in s or squareBracket in s:
            if parentheses in s:
                s = s.replace(parentheses,"")
            if curlyBracket in s:
                s = s.replace(curlyBracket,"")
            if squareBracket in s:
                s = s.replace(squareBracket,"")


        if s is "":
            return True
        else:
            return False

```


# Approach 2: stack

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
看了答案之后的思路，对于任何valid string有以下几个特征：
- number of opening brackets is equal to number of closing brackets
- for every closing bracket you met, it must be the pair of the very last opening bracket you met.


## Approach
<!-- Describe your approach to solving the problem. -->
- emulate a `stack` using python list
- create a hash for storing pairs info.
- traverse every element in the string


## Complexity
- Time complexity: $O(n)$, one-pass solution
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$, for stack
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```
class Solution:
    def isValid(self, s: str) -> bool:
        # use list to emulate array-based stack
        stack = []

        # a hash with closing bracket as keys and opening bracket as value
        mapping = {
                    "}":"{",
                    "]":"[",
                    ")":"("    
                  }

        # traverse every element in the string
        for char in s:
            if char in mapping.keys():
                # 这个字符是closing bracket
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "dummy"
                
                if mapping[char] != top_element:
                    # 错位了,对不上号 
                    return False
            else:
                # 这个字符是opening bracket
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
        
```