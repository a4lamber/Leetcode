"""
双链表有以下几个区别:
- 每一个node变为了two way node. 
Node: data|pointer
TwoWayNode: pointer|data|pointer
- 可以指向previous node, traverse to the left;
- 多了一个tail node, 直接指向last node;
"""

class Node:
    def __init__(self,data =None,next = None):
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self,data,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous = previous
        
class DLinkedList:
    """
    Do one without dummy header node
    """
    def __init__(self):
        # Construct an empty doubly linked list
        self.head = None
        self.tail = None
                
        # self.head = TwoWayNode(None)
        # self.tail = TwoWayNode(None)
        # self.head.next = self.tail
        # self.tail.previous = self.head
    def insert_at_end(self,newItem):

        """
        Insert at the end of doubly linked list (DLL); 双链表的好处是，设计了
        一个tail pointer, 指向end of the DLL, 所以可以直接insert value, 时间复杂度
        为O(1)
        Args:
            newItem (_type_): data you wish to insert
        """
        # if the linked list is empty
        if self.head is None:
            node = TwoWayNode(newItem)
            self.head = node
            self.tail = self.head
        else:
            # 如果链表为非空
            # construct a new two way node, points to self.tail
            # points self.tail to the "new" tail now
            self.tail.next = TwoWayNode(newItem,self.tail)
            self.tail = self.tail.next
            
    def insert_at_start(self,newItem):
        
        if self.head is None:
            # if empty, it's the first node, |null|data|null|
            node = TwoWayNode(newItem)
            self.head = node
            self.tail = self.head
        else:
            # DLL is not empty, then
            # 1. 创建一个新node, next pointer 指向self.head, previous pointer指向null
            # 2. set previous pointer of the self.head to the newly created node
            # 3. point the self.head to the new node
            node = TwoWayNode(data = newItem,
                              previous = None,
                              next = self.head)
            self.head.previous = node
            self.head = node

    def remove_at_beginning(self):
        """
        remove node at the start of the linked list, O(1)
        Returns:
            _type_: data stored in the removed node (start node)
        """
        if self.head != None:
            removedItem = self.head.data
            self.head = self.head.next
            return removedItem    
    
    def remove_at_end(self):
        """
        remove node at the end of the linked list, O(1)
        Returns:
            _type_: data stored in the removed node (end node)
        """
        if self.head != None:
            # 1.将last node的数据存在removedItem中
            # 2.将tail node指向second last node
            # 3.将tail node的next pointer指向null, 切断和removed node的connection, 交给garbage collector
            removedItem = self.tail.data
            self.tail = self.tail.previous
            self.tail.next = None
            return removedItem
    
    def print_forward(self):
        """
        print the graphical representation of the linked list
        
        None<->5<->9<->3<->2<->None
        """
        llstr = ""
        # 判断是否为null
        if self.head is None:
            llstr = "the linked list is empty"
        else:
            # 如果不为null
            llstr += "None" + "<->"
            probe = self.head
            while probe != None:
                llstr += str(probe.data) + "<->"
                probe = probe.next
            
            llstr+="None"

        print(llstr)

    def print_backward(self):
        """
        prin the linked list from tail, in reverse order
        """
        llstr = ""
        if self.head is None:
            print("the linked list is empty")
        else:
            # it's not empty
            llstr += "None" + "<->"
            probe = self.tail
            while probe != None:
                llstr += str(probe.data) + "<->"
                probe = probe.previous
            
            llstr += "None"
            print(llstr)

    def remove_at(self,index):
        """
        remove data at certain index, O(n) on average since needs to traverse the linked list
        Args:
            index (_type_): _description_
            
        优化思路: 实际上根据index更靠近start index or end index, 我们可以判定一下
        traverse from start or reverse, 这样的话就能改善average时间复杂度;
        """
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        elif index == 0:
            # remove from the beginning
            self.head = self.head.next
        else:
            
            # traverse from the top
            probe = self.head
            counter = 0
            
            while probe != None:
                if counter == index - 1:
                    break
                counter += 1
                probe = probe.next 

            # 如果要removed index为i, 现在在i-1
            probe.next = probe.next.next
            probe.next.next.prev = probe
    
    def insert_at(self,index,newItem):
        # 看一下index是否valid
        if index < 0 or index >= self.get_length():
            raise Exception("index out of range")
        elif index == 0:
            self.insert_at_start(newItem)
        else: 
            probe = self.head
            counter = 0
            while probe.next != None:
                if counter + 1 == index:
                    break
                
                counter += 1
                probe = probe.next
            
            # 现在在i-1, 想插入的i
            node = TwoWayNode(data = newItem,
                              previous=probe,
                              next = probe.next)
            probe.next.previous = node
            probe.next = node
                
    def insert_values(self,dataList):
        pass    
            
    def get_length(self):
        """
        return length of the linked list
        Returns:
            _type_: _description_
        """
        # set a counter to count each node in linked list
        counter = 0
        # scan from the top
        probe = self.head
        while probe != None:
            counter += 1
            probe = probe.next
        
        return counter




if __name__ == "__main__":
    # test insert at start
    ll = DLinkedList()
    ll.insert_at_start(2)
    ll.insert_at_start(3)
    ll.insert_at_start(9)
    ll.insert_at_start(5)
    ll.print_forward()
    print("")
    
    # test remove at beginning
    ll.print_forward()
    print("removed item: " + str(ll.remove_at_beginning()))
    ll.print_forward()
    print("")

    # test remove at end
    ll.print_forward()
    print("removed item: " + str(ll.remove_at_end()))
    ll.print_forward()
    print("")
    # test remove at
    ll.insert_at_start(1)
    ll.insert_at_start(2)
    ll.insert_at_start(7)
    ll.insert_at_start(8)
    ll.print_forward()
    ll.remove_at(0)
    ll.print_forward()
    # test insert_at
    ll.print_forward()
    ll.insert_at(0,100)
    ll.print_forward()
