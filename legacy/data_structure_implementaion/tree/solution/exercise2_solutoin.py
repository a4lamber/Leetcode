'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-10 14:22:52
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-02-10 14:23:22
 # @ Description: solution 2 of the genereal tree problem
 '''
 
class TreeNode:
    """
    Implementation of general tree.
    """
    def __init__(self,data):
        # node contains two piece of data
        self.data = data
        
        # define parent and children of the node
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
             
    
    def print_tree(self,level):
        """
        bash style tree print up to certain layer
        Args:
            layer (_type_): _description_
        """
        
        # 先考虑boundary, from current level to specified level
        
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
                # 比较现在在第几层 with specified level
                if child.get_level() > level:
                    return
                
                child.print_tree(level)
        
    


def build_product_tree():
    # level 0
    root = TreeNode("Global")
    
    # level 1
    india = TreeNode("India")
    usa = TreeNode("USA")

    # connect 0 with 1
    root.add_child(india)
    root.add_child(usa)
    
    # level 2
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karataka")
    
    newjersey = TreeNode("New Jersey")
    cali = TreeNode("California")
    
    # connect 1 with 2
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(newjersey)
    usa.add_child(cali)
    
    # level 3 in india
    ahmed = TreeNode("Ahmedabad")
    baroda = TreeNode("Baroda")
    bangluru = TreeNode("Bangluru")
    mysore = TreeNode("Mysore")
    
    # connect 3 with 2 in india
    gujarat.add_child(ahmed)
    gujarat.add_child(baroda)
    karnataka.add_child(bangluru)
    karnataka.add_child(mysore)
    
    # level 3 in usa
    princeton = TreeNode("Princeton")
    Trenton = TreeNode("Trenton")
    Sanfran = TreeNode("San Francisco")
    Mountain = TreeNode("Mountain View")
    Palo = TreeNode("Palo Alto")
    
    # connect level 3 to 2 in usa
    newjersey.add_child(princeton)
    newjersey.add_child(Trenton)
    cali.add_child(Sanfran)
    cali.add_child(Mountain)
    cali.add_child(Palo)
    
    
    return root

root = build_product_tree()
root.print_tree(1)

