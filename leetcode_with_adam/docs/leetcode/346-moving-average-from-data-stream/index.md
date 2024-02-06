```python
from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque([])
        self.curr_sum = 0

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.curr_sum += val            
        else:
            # window is full
            prefix = self.window.popleft()
            self.window.append(val)
            self.curr_sum = self.curr_sum - prefix + val
        
        return self.curr_sum/len(self.window)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```