---
tags:
    - Array
    - Queue
    - Simulation
    - Sorting
---

# 950 Reveal Cards In Increasing Order

## Approach 1 Simulation with Queue

我们知道出来的顺序，要反推出什么样的顺序可以得到这个结果，我们可以用一个deque来模拟这个过程.

- 建一个deque，里面放0..n-1的index
- 构造一个result数组，长度为n, 用来存放最后的结果
- 对deck进行排序
- 对deck中的每一个card，
    - 我们从deque的左边取出一个index，然后将card放到result中这个index的位置
    - 只要deque不为空，我们就将deque左边再取出一个index，然后放到deque的右边


```python
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        # 0..n-1 所有的index
        queue = deque([i for i in range(n)])

        deck.sort()
        
        result = [0 for _ in range(n)]

        for card in deck:
            # reveal card from left end
            result[queue.popleft()] = card
            
            if queue:
                queue.append(queue.popleft())
        
        return result
```