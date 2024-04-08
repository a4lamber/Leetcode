# [3106 Lexciographically Smallest String After Operations with Constraint](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description/)


## Approach 1

we need to find the smallest string `t` possible w.r.t. original string `s`. By smaller, we always trying to place smaller alphabet in earlier of the string. For example,

```
s = 'zzzba'
# option 1,replace first char
t = 'azzba'
# option 2, replace second char
t = 'zazba'
```
From `s` to option 1 and option 2, it costs the same distance but t in option_1 is smaller than t in option 2. So intuition is that

- it's more cost-effective spend distance on early position of the string

Secondly, since the distance calculation is cyclic and we have 26 alphabet. The maximum distance between 2 character will be 13. U need to construct a helper function for that.

Algorithm:

- create a `helper(a,b)` to calculate the distance between character `a` and `b`
- maintain a `curr` for current distance so far. It needs to be smaller than `k`
- traverse the string from start to end O(n)
    - iterate over 26 alphabets O(26) to find the first character (also the smallest) that will have the `curr total distances <= k`
    - if `found`, we append the best candidate character
    - if `not found`, we append the character from original string


### Code Implementation
```python
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        curr = 0 
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        def distance(a,b):
            # get the distance between character a and b
            if abs(ord(a) - ord(b)) <= 13:
                return abs(ord(a) - ord(b))
            else:
                return 26 - abs(ord(a) - ord(b))
                
                        
        res = []
        curr = 0
        for i,c in enumerate(s):
            found = False
            for alphabet in alphabets:
                if distance(c,alphabet) + curr <= k:
                    curr = distance(c,alphabet) + curr
                    found = True
                    res.append(alphabet)
                    break
                
            if not found:
                res.append(c)
        
        return "".join(res)
```