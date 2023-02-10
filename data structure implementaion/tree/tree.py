'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-10 11:57:35
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-02-10 11:57:50
 # @ Description: implement of tree, genereal
 '''
 

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    
def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptops")
    
    root.add_child(laptop)
    
    return root

root = build_product_tree()
