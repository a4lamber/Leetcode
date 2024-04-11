---
tags:
    - String
    - Monotonic Stack
    - Greedy
    - Stack
---

# 402 Remove K Digits

单调栈很好的题目, 也有很多edge case需要处理. Edge case包括:

- one pass后发现k>0, 说明stack中的元素是递增的, 需要从stack尾部删除k个元素
- 最后的solution stack可能是`[0,0,0,0,0]`, 需要去掉leading 0s. 去完leading 0s后如果为空, 返回"0". 这些0来源于每次遇到0的时候, 会把stack中的元素全部弹出.

## Approach 1: Monotonically Increasing Stack

维护一个单调递增的栈，当遇到一个数字比栈顶元素小的时候(出现downhill)，就把栈顶元素弹出，直到栈顶元素比当前数字小或者栈为空，然后把当前数字压入栈中。这样可以保证栈中的元素是单调递增的。

每次出栈都decrement k，直到k为0或者栈为空。最后，如果k还大于0，说明栈中的元素是递增的，需要从栈尾部删除k个元素, 因为这时候的stack是一个递增的序列，删后面的更划算。

!!! tip
    k == 0后，后面的数字不管三七二十一，全都要.

最后，把栈中的元素拼接成字符串，去掉leading 0, 如果为空则返回"0"。

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # remove last k digits if k > 0 (increasing digits)
        res = stack[:-k] if k else stack

        # remove all leading zeros
        final = "".join(res).lstrip('0')
        
        return final if final else "0"
```