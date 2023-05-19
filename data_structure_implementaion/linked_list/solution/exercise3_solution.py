"""
Solution of problem 3, You need to implement singly linked list class with dummy header
node. Then you should compare with the class without implementing without dummy header
node.
"""
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
        
class SLinkedList:
    def __init__(self):
        # initialize the linked list with dummy header node
        self.head = Node(None,None)
        self.head.next = self.head
    
    def get_length(self):
        counter = 0
        probe = self.head