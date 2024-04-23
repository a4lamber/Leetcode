---
tags:
    - Array
    - Hash Table
    - String
    - Breadth-First Search
---
# 752 Open the Lock

很新颖的一道BFS题目了. 有点像gym lock, 有四位数，不断换位，但是有些位是deadend, 不能换位。我们要找到最少的换位次数，从"0000"到"target"。

![](./assets/1.excalidraw.png)

在matrix中的上下左右四个方向，这里变成了8个方向，因为每个数字可以加1或者减1，所以有8个状态量. Similarly, 需要维护一个set来记录已经访问过的状态量，避免重复访问。BFS最先到达的状态量肯定是最短路径。

!!! warning "warp-around的处理"
    这8个状态量计算时要注意wrap around以及减法时候的负数处理。
    
    - 0 + 1 = 1, 1 % 10 = 1
    - 9 + 1 = 10, 10 % 10 = 0 (wrap around 9-->0)
    - 0 - 1 = -1, (-1 + 10) % 10 = 9 (wrap around 0-->9)


## Approach 1 BFS

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        observation:
        - kinda like gym lock from 0-9 but 9 wraps around to 0
        - starts from "0000" --> "target"
        - 要避开中间deadend state
        - 有点像tree,但是有些路被封掉了
        """
        def bfs(lock):
            """
            return a list of next state, if input is '0000'
            output is ['0001','0009','0010','0090',......]
            """
            res = []
            for i in range(4):
                digit_increment = lock[:i] + str((int(lock[i]) + 1 + 10)%10) + lock[i+1:]
                res.append(digit_increment)
                digit_decrement = lock[:i] + str((int(lock[i]) - 1 + 10)%10) + lock[i+1:]
                res.append(digit_decrement)
            return res
        
        # edge case
        if '0000' in deadends:
            return -1
        
        q = collections.deque()
        # lock stack, turn
        q.append(['0000',0])
        visited = set(deadends)

        while q:
            state,turn = q.popleft()
            # base case
            if state == target:
                return turn            
            # doing BFS
            for child in bfs(state):
                if child not in visited:
                    visited.add(child)
                    q.append([child,turn+1])
        # whoops not found
        return -1
```