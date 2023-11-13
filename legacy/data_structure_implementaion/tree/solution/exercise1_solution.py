'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-10 13:31:39
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-02-10 13:32:43
 # @ Description: solution to question 1, a general tree that takes in two value.
 '''
class TreeNode:
    """
    Implementation of general tree.
    """
    def __init__(self,name,designation):
        # node contains two piece of data
        self.name = name
        self.designation = designation
        
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
             
    
    def print_tree(self,key):
        """
        bash terminal like directory print
        """
        hashtable = {
                        "name":self.name,
                        "designation": self.designation,
                        "both": self.name + " (" +self.designation + ")"
                    }
        
        if key not in hashtable.keys():
            raise Exception("The key input is invalid, must be name, designation or both")
            
        
        
        if self.get_level() == 0:
            # its' root level
            spaces = ""
        else:
            # it's not root level
            spaces = "|   " * (self.get_level()-1) + "|-- " * 1
        
        # call the print function
        print(spaces + hashtable[key])
        
        # recursive call print_tree()
        if len(self.children) > 0:
            # if it's not leaf node, recursively call print_tree()
            for child in self.children:
                child.print_tree(key)
        
    


def build_product_tree():
    # level 0
    ceo = TreeNode("Nilupul","CEO")

    # level 1, CTO sub-tree
    cto = TreeNode("Chinmay","CTO")
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    app_head = TreeNode("Aamir","Application Head")
    cloud_manager = TreeNode("Dhaval","Cloud Manager")
    app_manager = TreeNode("Abhijit","App Manager")
    # connect
    cto.add_child(infra_head)
    cto.add_child(app_head)
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)
    
    # level 1, HR Head sub-tree
    hr_head = TreeNode("Gels","HR Head")
    recru_manager = TreeNode("Peter","Recruitment Manager")
    policy_manager = TreeNode("Waqas","Policy Manager")
    # connect level 2 to 1
    hr_head.add_child(recru_manager)
    hr_head.add_child(policy_manager)
    
    # connect level 1 with 0
    ceo.add_child(cto)
    ceo.add_child(hr_head)
    
    
    return ceo




root = build_product_tree()
# root.print_tree(key = "name")
# root.print_tree(key = "designation")
root.print_tree(key = "both")
