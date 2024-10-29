---
tags:
    - Stack
    - Design
---
# [155 Min Stack](https://leetcode.com/problems/min-stack/description/)

设计类题目，姐妹题为[716 max stack](https://leetcode.com/problems/max-stack/description/?envType=company&envId=lyft&favoriteSlug=lyft-all). 

这题tricky的地方在于怎么用array来实现$O(1)$ for push(), pop(), peek() and get_min(). Especially get_min().

|approach|description|time|space|
|-|-|-|-|
|one stack emulation|store minimum value at all snapshot in history. Use one stack to store tuple `(curr_val,global_min)`|$O(1)$|$O(2n)\approx O(n)$|
|two stack|maintain a monotonically decreasing stack. Only store minimum value if the new element is $\leq$ the smallest value so far|$O(1)$|$O(n)$|
|two stack better|Instead, store a counter of how many times we encounter it|$O(1)$|$O(n)$|

## Intuition

[Stack](../../data_structure/stack/index.md)作为基础的数据结构，有两种方式来emulate

- emulate with array
- emulate with linked list

For this question, the hardest part is that we need to have $O(1)$ for 

- push()
- pop()
- top(): it's peek() in disguise
- getMin()

If we think about min-heap, it only has $O(nlogn)$ for retrieving the minimum value, which is slower than our design goal. So we rule this out.

So we can't use heap, we don't use linked list a lot in day to day work So it is highly likely we gonna use `array`. But how to allow us the `getMin()` in $O(1)$, we have to understand two things:

- time-space tradeoff is first thing pops in my mind
- we don't necessarily need to maintain a sorted order of all the arr elements. But we do need **some history of the min along with the actual value**.


## Approach 1 Stack of tuples

we can maintain a stack like

$$
\begin{equation}
[(x_0,min_{t_{0}}),(x_1,min_{t_{1}}),(x_2,min_{t_{2}}),\dots,(x_n,min_{t_{n}})]
\end{equation}
$$
where $x_n$ is the value at the top of the stack, $min_{t_{n}}$ is the smallest value among $\min \{ x_0, x_1, \dots, x_n \}$.

Or in another words, smallest value among all values to the left of it until the bottom of stack.

### Code Implementation

```python
# use array to emulate it. If use heap, it's O(nlogn) for getting min value, not good
class MinStack:
    """
    O(1) for all functions. To achieve O(1), we have to trade speed with space.
    We maintain a list of tuple (val,curr_global)
    
    [(val,min_at_t_0),(val,min_at_t_1),(val,min_at_t_2),....,(val,min_at_t_n)]
    """
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        """push to the stack"""
        if not self.stack:
            self.stack.append((val,val))
            return
        _, curr_min = self.stack[-1]
        # write the current min after we insert this guy
        self.stack.append((val,min(val,curr_min)))
    def pop(self) -> None:
        """pop the top element of the stack. Not necessarily the minimum element
        """
        self.stack.pop()

    def top(self) -> int:
        """peek the top of the stack
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """return the minimum value in the stack so far
        """
        return self.stack[-1][1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## Approach 2 With Two Stack

按照approach 1的逻辑，假如我们的min value一直不变, for example

`self.stack = [(1,1),(2,1),(3,1),...,(100,1)]`

没发现我们一直在重复的存redudant min, `1` in this case. 这就有了优化的余地，类似于sparse matrix的压缩储存方式. 

![](https://images.javatpoint.com/ds/images/sparse-matrix7.png)

我们可以maintain 

- `self.stack`: for all the values we need to store in our class
- `self.min_stack`: an monotonically decreasing (不需要strict) stack that only store value if it's smaller than the minimum value/last value


### Code Implementation

```python
class MinStack:
    def __init__(self):
        self.stack = []
        # monotonically decreasing stack (not strict)
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## Approach 3 With Two Stack on steroid

```python
self.min_stack = [10,10,2,1,1,1,1,]
```

We can further compress it down to with a `counter` variable

```python
self.min_stack = [[10,2],[2,1],[1,4]]
```

### Code Implementation

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # empty or smaller than last val in self.min_stack
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val,1])
        elif val == self.min_stack[-1][0]:
            # case we can insert to min_stack
            self.min_stack[-1][1] += 1
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1][0]:
            # decrement the counter by one
            self.min_stack[-1][1] -= 1
            # if nothing left
            if self.min_stack[-1][1] == 0:
                self.min_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1][0]
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```