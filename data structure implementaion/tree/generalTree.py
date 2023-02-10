'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-10 11:57:35
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-02-10 11:57:50
 # @ Description: implement of tree, genereal
 # the goal of this script is to constrcut a tree like shown here
 '''
 

class TreeNode:
    """
    Implementation of general tree
    """
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    
    def get_level(self):
        """
        return the level this node is at. Note root is in level 0
        
        Returns:
            _type_: the level the current node is at
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
             
    
    def print_tree(self):
        """
        bash terminal like directory print
        """
        if self.get_level() == 0:
            # its' root level
            spaces = ""
        else:
            # it's not root level
            spaces = "|   " * (self.get_level()-1) + "|-- " * 1
        
        # call the print function
        print(spaces + self.data)
        
        # recursive call print_tree()
        if len(self.children) > 0:
            # if it's not leaf node, recursively call print_tree()
            for child in self.children:
                child.print_tree()
        
    


def build_product_tree():
    # construct a root
    root = TreeNode("Electronics")
    
    # laptop at level 1
    laptop = TreeNode("Laptops")
    macbook = TreeNode("Macbook")
    micro_surface = TreeNode("Microsoft surface")
    thinkpad = TreeNode("Thinkpad")
    laptop.add_child(macbook)
    laptop.add_child(micro_surface)
    laptop.add_child(thinkpad)
    
    # cell phone at level 1
    cellphones = TreeNode("Cell Phones")
    iphone = TreeNode("iphone")
    google_pixel = TreeNode("google pixel")
    vivo = TreeNode("vivio")
    cellphones.add_child(iphone)
    cellphones.add_child(google_pixel)
    cellphones.add_child(vivo)
    
    # television sub-tree at level 1
    television = TreeNode("Televisions")
    samsung = TreeNode("Samsung")
    lg = TreeNode("LG")
    television.add_child(samsung)
    television.add_child(lg)
    
    
    # connect root with level 1 node
    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(television)
    
    
    return root




root = build_product_tree()
root.print_tree()
