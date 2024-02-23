---
tags:
    - Arraty
    - Stack
    - Monotonic Stack
---
# 1762 Buildings With an Ocean View


## Approach 1 Monotonic Stack

需要寻找对每一个building with index `i`, 在`heights[i+1:]`中没有任何一个`heights[j]`满足`heights[j] > heights[i]`的`i`. Return a list of those indices. 

我们可以求它的补集, 当你用monotonic stack来寻找最大值时，有两个findings:

- 找到最大值的都被pop掉了
- 找不到最大值的都在stack里

```python
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # monotonical stack with longer building at the bottom, if found, then we don't want it
        stack = list()
        # when the value is poped, that popped value has been blocked and has not ocean view
        for i,height in enumerate(heights):
            while stack and height >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        

        return stack
```