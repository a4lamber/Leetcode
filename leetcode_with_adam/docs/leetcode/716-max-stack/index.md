---
tags:
    - Stack
    - Design
    - Linked List
    - Doubly-Linked List
    - Ordered Set
---

# [716 Max Stack](https://leetcode.com/problems/max-stack/description/)

## Intuition
design类题目，implement max stack. 需要的功能为:

- `pop()`
- `top()`
- `peekmax()`
- `popmax()`

我们先讲大思路, implement stack有两种方式linkedlist or array, 但这题有两个hint, 分别是

- implement max `top()` with `O(1)`, others with `O(logn)`
- keep track of max value

那我们首先想到的就是max heap. 那我们手上就有三个候选数据结构, max heap, array and linked list. 平时工作用不到linkedlist, 那么就先看看array alone能否解决这个问题，或者解决这个问题的难点在哪里

!!! note "只用array行不行? why"
    难点在于pop()和popmax()时，你如果用两个array来track最大值 like in 155 min stack, 
    
    - array 1: for storing 
    - array 2: monotonically increasing array, 只记录value>=目前的最大值

    你会遇到一个困境就是pop() element from array 1之后，没法知道怎么pop element from array 2. 但这个可以用一个unique idx + hashset来解决
    ```python
    self.stack = []
    self.max_stack = []
    self.removed = set()
    self.uuid = 0
    ```
    我们每次push(),都会increment self.uuid by 1. 然后我们同时保存tuple of (idx,val) into our array. 这样似乎也能接受? 但实际上并不然，比如这个scenario. 你push()五次，然后popmax()5次，实现的functionality和pop()五次后一样。那么你array 2必须要保存true copy of each data. 同时又要求`O(logn)`, array 2没法达到性能要求. 那就只能用max heap to keep track of descending orders了.

由此我们第一个思路就是max heap + array.

## Approach 1 Heap + Lazy Update

比较难理解的是lazy update, do it when it is absolutely necessary. 倒不如叫拖延症strategy.但换句话说, 哪个节点是absolutely necessary?

- `push()`: 没有节点
- `pop() -> int`: 有影响，需要把potential prior `popmax()`的欠债还清
- `top() -> int`: 有影响，需要把potential prior `popmax()`的欠债还清
- `popmax() -> int`: 有影响，需要把potential prior `pop()`的欠债还清
- `peekmax() -> int`: 有影响，需要把potential prior `pop()`的欠债还清

不然return的数据就不对了.

```python
from heapq import heappush,heappop
class MaxStack:
    def __init__(self):
        self.heap = []
        self.stack = []
        self.removed = set()
        self.uuid = 0
        
    def push(self, x: int) -> None:
        self.stack.append((x,self.uuid))
        heappush(self.heap,(-x,-self.uuid))
        self.uuid += 1
        
    def pop(self) -> int:
        """
        O(1) for now, lazy-update later with O(logn)
        """
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

        num,idx = self.stack.pop()
        self.removed.add(idx)
        return num
        
    def top(self) -> int:
        """
        """
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
        
    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heappop(self.heap)
        num,idx = heappop(self.heap)
        self.removed.add(-idx)
        return -num

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
```