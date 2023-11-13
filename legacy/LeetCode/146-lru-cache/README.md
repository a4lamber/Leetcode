# Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
- `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
- `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

## Example1
```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## Approach

> 实现LRU, 往往是通过HashMap + doubly linked list

我们可以break down每一个需求:
- `LRUCache(int capacity)`: constructor for the cache, 有一定的大小限制;
- `int get(int key)` search for an key, if yes, return it if no, return -1. 首先想到的就是linear search, binary search and hash, 既然题目里要求了O(1), it's a dead give-away that we need to use hash.
  
- `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key. 这个比较复杂，我们分三种情况讨论:
  - if key exists in key-space, we update it if necessary
    - 我们可以简化成`remove` the node, then `insert` the node
  - if key doesn't exist in key-space, add it
    - just `insert` the node. 可以和上一步并成一步；
  - if it's over capacity, we remove the least recently used (LRU)
    - 给我们一个概念是要按照有无access过，来排序，解决思路是每一次call methods `get()` and `put()`, 只要运行成功，我们都把它挪到链表一端


**The functions get and put must each run in O(1) average time complexity.**

## Solution
```python
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # will node be automatically collected?

    # insert the right hand side
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # it's in key space
            # update the least usage (remove and insert)
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value

        # not found
        return -1
        

    def put(self, key: int, value: int) -> None:
        # it it's in key space
        # it's not in key space
        # it's over capacity
        if key in self.cache:
            self.remove(self.cache[key])
        
        # create a new node
        node = Node(key,value)
        # put it in the hash
        self.cache[key] = node
        # insert the node to the right-mose
        self.insert(node) # you could use self.insert(self.cache[key]), they both points to the same node

        # delete the least recently used, insert the new node
        if len(self.cache) > self.capacity:
            # delete lru, evict space on the hash
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

# Reference 
- [考博](https://www.jiakaobo.com/leetcode/146.%20LRU%20Cache.html)
- [neetcode](https://www.youtube.com/watch?v=7ABFKPK2hD4&ab_channel=NeetCode)