
# [3099 Harshad Number](https://leetcode.com/problems/harshad-number/description/)


```python
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        """
        - calculate sum of its digits
        - if harshad number
            - return sum of digits
        - else
            - return -1
        """
        res = -1
        nums = str(x)
        total_sum = 0
        for num in nums:
            total_sum += int(num)
        
        if x%total_sum == 0:
            return total_sum
        else:
            return -1
```