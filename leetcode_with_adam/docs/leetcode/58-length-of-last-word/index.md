---
tags:
    - String
---
# [58 Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/)

This question is kinda tricky, and i will introduce three solution 

- split and then get the last word, $O(n)$ in time, $O(n)$ in space
- two pass solution $O(n)$ in time, $O(1)$ in space
- one pass solution $O(n)$ in time, $O(1)$ in space


## Approach 1: Naive Solution

This is the solution came to my mind when i saw it. $O(n)$ in time, $O(n)$ in space.

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(" ")

        for i in range(len(res)-1,-1,-1):
            if len(res[i]) != 0:
                return len(res[i])
```

## Approach 2: two pass solution

We realize that there are some trailing zeros that we need to handle and it is giving us some troubles. Our two passes are:

- `1st pass`: First "trim" the trailing white space by decrementing `tail` pointer. 
- `2nd pass`: Then we calculate the length of the last word by incrementing `res`.

This solution is $O(n)$ in time and $O(1)$ in space.

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # two-pass, 1 for triming right white space, 2nd for computing length
        # 1st pass: "trim" right white space
        tail = len(s) - 1
        while tail >= 0 and s[tail] == " ":
            tail -= 1
        
        # 2nd pass: calculate length of last world
        res = 0
        while tail >= 0 and s[tail] != " ":
            res += 1
            tail -= 1
        return res
```

## Approach 3: one pass solution

After you understand the two pass solution, you will realize that it must exist a one pass solution. The obstacle is that we need to handle the trailing white space and the white space between last word and 2nd last word. As illustrated in the figure below,

![](assets/1.excalidraw.png)

The trick is that, we need to calculate length anyways. so we have two variables:

- `res` to store the length of last word
- `tail` to store the current index we traversing from end of the string

When we are in first white space (trailing white space), 

- `res == 0` is always true
- `tail` is just decrementing until we reach the end of last word i.e. `s[tail] != " "`
- `s[tail] == " "` is always true

While we are in the 2nd white space, (white space between last word and 2nd last word)

- `res != 0` is always true
- `tail` is just decrementing until we reach the end of 2nd last word i.e. `s[tail] != " "`
- `s[tail] == " "` is always true

Therefore, we can see that the only difference is the `res` between the two white spaces. So we can just use `res` as the escape condition for distinguishing the two white spaces.

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # one pass solution, calculat none " " white space
        tail = len(s) - 1
        res = 0

        while tail >= 0:
            if s[tail] != ' ':
                res += 1
            elif res > 0:
                return res            
            tail -= 1
            
        return res
```










