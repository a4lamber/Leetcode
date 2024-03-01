---
tags:
    - Math
    - String
    - Greedy
---

# [2864 Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number/description/?envType=daily-question&envId=2024-03-01)

Bit manipulation + Greedy. but i used the hashmap


## Approach 1 Hashmap

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # odd number, last digit must be 1
        c = collections.Counter(s)
        
        num_of_ones = c["1"]
        res = []

        
        while num_of_ones > 1:
            print(num_of_ones)
            res.append("1")
            num_of_ones -= 1
        
        num_of_zeros = c["0"]
        while num_of_zeros > 0:
            res.append("0")
            num_of_zeros -= 1
        
        res.append("1")
        
        return "".join(res)    
```

