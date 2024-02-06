# Approach 1 with array

```python
class MyCircularQueue:
    """
    Use array to implement "circular "queue. Imagine we have a full queue like 
    [1, 2, 3, 4 ,5 ]
    and we execute two dequeue() from the top. 
    [_, _, 3, 4 ,5 ]
    Now, we have some space near the head but we don't have space at the tail. 
    It will cause problem if we decide to enqueue(i), we will be
    - shifting everything to fill the empty space near head of the queue (O(n))
    - expand the fix-sized array, (create an array of size 2n, move to it, destroy the old array)
    """
    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.count = 0
        self.capacity = k
        # always points to the head of the queue
        self.head = 0
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue from tail. Return true if the operation
        is successful. Return false if the queue is maxed out.
        """
        if self.count == self.capacity:
            return False
        # last available slot ready to be enqueued
        tail_enqueue = (self.head + self.count) % self.capacity
        self.queue[tail_enqueue] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Pop an element from the head. Return true if the operation is successful.
        Return false if the queue is empty
        """
        if self.count == 0:
            return False
        # remove the element at head
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        # points to last item in the queue (who just enqueued)
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]
        
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```