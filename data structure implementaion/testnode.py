'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2022-09-16 10:25:26
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2022-09-16 10:25:33
 # @ Description: initialize an singly linked structure of size 6 
 # using node class.
 '''
 
from node import Node
 
 
# define a head node, the item with index 0
head = None

# 俄罗斯套娃 node nested in a node for index 1 to 5
for i in range(1,6):
    head = Node(i,head)

# traverse through the 
while head != None:
    print(head.data)
    head = head.next