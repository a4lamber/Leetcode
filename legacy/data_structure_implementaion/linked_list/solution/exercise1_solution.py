"""
solution for code
"""


class Node:
    def __init__(self,data =None,next = None):
        self.data = data
        self.next = next


class SLinkedList:
    def __init__(self):
        # construct an empty linked list
        self.head = None
        
    def insert_at_begining(self,newItem):
        """
        Insert operation at the beginning of the linked list, O(1)
        
        Args:
            newItem (_type_): data in the new node
        """        
        # create a new node, connects to self.head
        node = Node(newItem,self.head)
        
        # override self.head with node
        self.head = node
    
    def insert_at_end(self,newItem):
        """
        Insert at the end of linked list; Since you need to
        traverse to the end of the linked list, so O(n) 
        Args:
            newItem (_type_): value you wish to insert at the end;
        
        问题: 由于singly linked list有一个特性，你一旦traverse之后，
        就回不来了，所以insert的时候要创造一个shallow copy of it,
        然后insert at the end
        
        答案: 就正如你 a = [1,2,3,4] b = a 然后你traverse b一样,
        再怎么access b such as b[2], b[3] 都没用;
        """
        # create a tail link (empty)
        newNode = Node(newItem,None)
        
        if self.head is None:
            # 该linked list为空
            self.head = newNode
        else:
            # 该linked list不为空,则traverse to the end
            
            # 建一个shallow copy, called probe
            probe = self.head
            
            while probe.next != None:
                probe = probe.next
            
            # at last node of the linked list
            probe.next = newNode
    
    def remove_at_begining(self):
        """
        removes the item at the beginning and return the removed item
        Returns:
            _type_: the data in the head node
        """
        if self.head is not None:
            # 保证linked list中至少有一个数据点
            removedItem = self.head.data
            # go to next node
            self.head = self.head.next
            return removedItem
        
    def remove_at_end(self):
        """
        removes the item at the end of the linked list, then return it
        Returns:
            _type_: the data stored in the last node
        """
        probe = self.head
        
        while probe.next.next != None:
            probe = probe.next
        
        # 现在在linked list倒数第二个位置
        removedItem = probe.next.data
        # override the last node to be None;
        probe.next = None
        return removedItem
            
    def search(self,targetItem):
        """
        Search in the linked list for target value, O(n)

        Args:
            targetItem (_type_): target value you want to search
            for in the linked list
            
        Returns:
            boolean: if found, then true else one
        """
        # 设置一个dummy variable, 不修改self.head
        probe = self.head
        
        # 只要还没碰到stop sign 和target item则: 
        while probe != None and targetItem != probe.data:
            probe = probe.next
            
        # 到这一步只有两种可能, 1: 遇到none了, 2: 找到targetItem了
        if probe != None:
            # item found
            return True
        else:
            return False
    
    def get_length(self):
        """
        return the length of the linked list
        Returns:
            int: length of the linked list
        """
        counter = 0
        probe = self.head
        while probe != None:
            counter += 1
            probe = probe.next
        
        return counter
        
    def print(self):
        """
        print the graphical representation of the linked list
        1-->5-->6-->None
        """
        # llstr: linked list string, output msg
        llstr = ""
        
        # 判断链表是否为empty
        if self.head is None:
            llstr = "linked list is empty"  
        else:                
            # dummy variable
            probe = self.head
                        
            # traverse the linked list until the end
            while probe != None:
                llstr += str(probe.data) + "-->"
                probe = probe.next
            
            llstr += "None"
        print(llstr)

    def remove_at(self,index):
        """
        remove the particular node in the linked list based on id
        Linkedlist: 1-->2-->3-->None
        Index:      0   1   2
        
        Args:
            index (int): index you wish to remove from the linked list
        """
        probe = self.head
        
        if index < 0 or index>= self.get_length():
            raise Exception("Invalid index")
            
        # 考虑特殊情况， remove at the begining
        if index ==0:
            self.head = self.head.next
            return
        
        counter = 0
        probe = self.head
        
        while probe != None:
            # 如果要删除node i, 你只需要把node i-1和node i+1连接起来就可以了
            if counter == index -1:
                probe.next = probe.next.next
            
            probe = probe.next
            counter += 1
    
    def insert_at(self,index,newItem):
        """
        insert at i location, O(n) on average
        Args:
            index (_type_): index you want to insert at
            newItem (_type_): the data you want to insert

        Raises:
            Exception: input index is not valid;
            
        没有dummy header row, 太繁琐了，各种分类讨论;
        """
        # 检查index是否不符合标准
        if index<0 or index> self.get_length():
            raise Exception("invalid index")
        elif index == 0:
            # 直接在beginning插入的情况
            self.insert_at_begining(newItem)
        elif index == self.get_length():    
            self.insert_at_end(newItem)
        else:
            # shallow copy of linkedlist
            probe = self.head
            counter = 0
            
            
            while probe!= None:    
                if counter == index - 1:
                    break
                
                probe = probe.next
                counter += 1
            
            # 现在位置在要插入的index, i前一个,做以下两个操作
            # 1: point new node with node[i]
            # 2: point node[i-1] to the new node
            newNode = Node(newItem,probe.next)
            probe.next = newNode
        
    def insert_values(self,dataList):
        """
        erase the current linked list, insert.
        Since the data is inserted at end of the linkedlist,
        for a size n input list, the time complexity is O(n^2) 
        Args:
            dataList (_type_): _description_
        """
        # erase the previous linked list
        self.head = None
        for data in dataList:
            # insert the data to the end of it
            self.insert_at_end(data)
    
    # exercise 1 
    def insert_after_value(self,targetItem,dataItem):
        """
        search for data_after within the linked list, if exists, insert after the node
        
            targetItem (type): 你需要寻找的数
            dataItem (type): 你想要插入的数
        """
        
        probe = self.head
        
        # traverse and search for whether target within the 
        while probe!= None and probe.data != targetItem:
            probe = probe.next
        
        if probe != None:
            # 说明search到targetItem, 假设targetnode为node[i]
            # 1. 创建一个new node, 指向node[i+1]
            # 2. 将target node指向new node
            newNode = Node(dataItem,probe.next)
            probe.next = newNode
        else:    
            # 遇到none, 也就是运行到end of linked list也没找到
            raise Exception("targetItem not found")
        
    # exercise 2 
    def remove_by_value(self,targetItem):
        """
        search for dataItem, if exists remove it.
        注意corner cases, 第一个item和最后一个item
        Args:
            dataItem (_type_): _description_
        """
        
        # 判断第一个item是不是target Item
        if self.head.data == targetItem and self.head != None:
            self.head = self.head.next
            return
        
        probe = self.head     
        # traverse the linked list 
        while probe.next != None and probe.next.data != targetItem:
            probe = probe.next
        
        if probe.next != None:
            # 找到数据,在probe.next.data = targetItem
            probe.next = probe.next.next
        else:
            raise Exception("item not found, can't remove")
        
if __name__ == "__main__":
    """
    Just a bunch of random testing code
    """

    # ll = SLinkedList()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()