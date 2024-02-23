---
tags:
    - Array
    - Stack
    - Monotonic Stack
---


# [1475 Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/)

很好的monotonic stack的题目, 用stack来解决nearest smaller element的问题.


## Approch 1: Monotonic Stack


```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # ==> find next element smaller or equal to prices[i]
        stack = []
        ans = prices[:]
        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = prices[prev_index] - price
            
            stack.append(i)

        return ans
```