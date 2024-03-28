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


