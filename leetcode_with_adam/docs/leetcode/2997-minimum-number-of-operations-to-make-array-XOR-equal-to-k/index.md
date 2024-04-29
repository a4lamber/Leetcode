---
tags:
    - Array
    - Bit Manipulation
---

# 2997. Minimum Number of Operations to Make Array XOR Equal to Zero

## Approach 1 

To understand this problem a little bit better, and we write an example into the following format:

```
[2,1,3,4] 

010
001
011
100
---xor---
100

k = 1 = 001
```

We need to flip bits such that 100 --> 001.That's the essence of the problem. 

There is a key observation for XOR product:

- XOR product for odd number of 1's in the column, the result is 1
- XOR product for even number of 1's in the column, the result is 0


We just need to traverse every possible column and count the number of bits that need to be flipped. 

Algorithm

- Calculate the XOR of all elements in the array, `x`
- traverse every bit of `x` and `k` and count the number of bits that need to be flipped.

!!! note
    - Time Complexity: O(n)
    - Space Complexity: O(1)

### Code Implementation

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        1. choose any element (10进制 like 3 = 011)
        2. flip any bit of your choice (011 --> 111), ans = 7
        Observation:
        - for odd number of 1's the result is 1
        - for even number of 1's the result is 0
        """
        x = 0
        for num in nums:
            x ^= num
        
        count = 0

        for i in range(32):
            # a: x's i-th bit is set or not
            # b: k's i-th bit is set or not
            a = (x & (1 << i) != 0)
            b = (k & (1 << i) != 0)
            count += (a != b)
        return count
```