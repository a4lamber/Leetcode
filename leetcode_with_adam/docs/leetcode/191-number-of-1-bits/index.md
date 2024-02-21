---
tags:
    - Divide and Conquer
    - Bit Manipulation
---

# 191 Number of 1 Bits

这题是计算[hamming weight](https://en.wikipedia.org/wiki/Hamming_weight). 给的是一个32位的整数，计算这个整数的二进制表示中有多少个1, 所以我们需要做两件事,

- check if the last bit is 1
  - use `n & 1 = 1` to check if the last bit is 1 (same as check if it's odd)
- traverse the binary input by shift the bits to the right
  - `n >> 1` till `n=0`


## Approach 1 Bit Manipulation

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. check whether the last digit is 1
        #      n & 1 == 1 then yeahhhh
        # 2. traverse the bits
        #      n >> 1 until 
        counter = 0
        while n != 0:
            if n & 1 == 1:
                counter += 1            
            n = n >> 1
        
        return counter
```