---
tags:
    - Tree
    - Design
    - Binary Search Tree
    - Heap (Priority Queue)
    - Binary Tree
    - Data Stream
---

# 703 Kth Largest Element in a Stream

This question is asking for maintaining a data stream and return the kth largest element in the stream. Since we only interested in the kth largest element, we can just maintain kth largest elements in a DS by popping the smaller ones. Therefore, we can use a min heap of maximum length k to maintain the kth largest elements by popping the smaller ones.

```python
from heapq import heapify,heappush,heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        since the problem asks for return the kth largest element in the stream
        we only need to maintain a DS of len(k) and make sure those are the largest
        """
        heapify(nums)
        self.heap = nums
        self.k = k
        # we can get rid of the smaller values till length is k
        self._prune()
        
    def add(self, val: int) -> int:
        heappush(self.heap,val)
        self._prune()
        
        return self.heap[0]
    
    def _prune(self):
        while len(self.heap) > self.k:
            heappop(self.heap)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```