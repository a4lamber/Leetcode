---
tags:
    - Array
    - Queue
    - Sliding Window
    - Monotonic Queue
    - Heap (Priority Queue)
---
# [239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)


## Approach 1: Brute Force

Brute force solution would be slicing every window and take the maximum of each window. The time complexity would be `O(n*k)` where `n` is the length of the array and `k` is the window size.


## Approach 2: Monotonic Queue

既然是求sliding window最大值，我们可以用一个monotonically decreasing的queue来维护window内的最大值和单调性. 

```
queue: storing the "index" for an decreasing monotonic queue. 
res: 记录max index for monotonic queue
```

可以分成两个部分:

- 初始化第一个window
    - 如果新元素比queue中的最后一个元素大，pop掉最后一个元素，直到queue被清空或者新元素比queue中的最后一个元素小
    - 记录queue中的第一个元素到res中, 此时res长度为1
- 从第2个 to 第(n-k+1)个 window
    - 如果queue中的第一个元素已经离开当前window, pop掉第一个元素
    - 如果新元素比queue中的最后一个元素大，pop掉最后一个元素，直到queue被清空或者新元素比queue中的最后一个元素小
    - 把新元素的index加入queue
    - 记录queue中的第一个元素到res中, res长度 +1 直到res长度为n-k+1

!!! note 
    - time complexity: $O(n)$ 看上去像是for + while loop, 但实际上worst case scenario是每个元素都进出queue一次，所以是$O(2n) \approx O(n)$
    - space complexity: $O(k)$, queue的最大长度为k

### Code Implementation

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 求每一个window中的最大值，所组成的Array.
        queue = deque()
        res = []
        n = len(nums)

        # initialize the initial monotonic queue (in the first window of size k)
        for i in range(k):
            # pop 队列中小于新元素nums[i]的值, 直到结束
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        res.append(nums[queue[0]])

        for i in range(k,n):
            # 比较queue最左边值是否已经离开window
            if queue and queue[0] == i-k:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            # enque
            queue.append(i)
            res.append(nums[queue[0]])
        
        return res
```



