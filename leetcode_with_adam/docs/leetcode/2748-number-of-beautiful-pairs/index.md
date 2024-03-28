---
tags:
    - Array
    - Math
    - Number Theory
---
# 2748 Number of Beautiful Pairs

考点比较数学.

## Approach 1

复习了三个知识点:

- `math.gcd(a,b)` 求最大公约数 (greatest common divisor), if `gcd(a,b) == 1` 说明a,b互质
- last digit of a number `num % 10`
- first digit of a number `num // 10 until num < 10`


```python
import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        """
        1. enumeration
        2. math.gcd()
        """
        pairs = 0
        for j, num in enumerate(nums):
            # last digit for nums[j]
            last_digit = num % 10
            for i in range(j):
                first_digit = nums[i]
                # get first digit
                while first_digit >= 10:
                    first_digit //= 10
                pairs += math.gcd(last_digit,first_digit) == 1
        return pairs
```