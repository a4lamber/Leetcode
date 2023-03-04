class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        """
        Add a value into the BST (can't contain duplicate). Use BST could be used for constructing set() in python
        Args:
            data (_type_): _description_
        """
        if data == self.data:
            # BST can't have duplicate number
            return 
    
        if data < self.data:
            # add to left subtree
            # step 1 check if 
            if self.left:
                # left sub tree is not empty
                self.left.add_child(data)
            else:
                # left sub tree is empty. Place a node and plant there
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                # left sub tree is not empty
                self.right.add_child(data)
            else:
                # BST empty
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self,root):
        # left -> root -> right
        # fill this list with elements in BST with the specified order
        res = []
        
        if root:
            res += self.in_order_traversal(root.left)
            res.append(root.data)
            res += self.in_order_traversal(root.right)
        
        return res
                        
         
    def pre_order_traversal(self,root):
        res = []
        
        if root:
            res.append(root.data)
            res += self.pre_order_traversal(root.left)
            res += self.pre_order_traversal(root.right)
        
        return res
            
    def post_order_traversal(self,root):
        res = []
        
        if root:
            res += self.pre_order_traversal(root.left)
            res += self.pre_order_traversal(root.right)
            res.append(root.data)
        
        return res
    
    
    def search(self,value):
        # O(logn) search 
        
        if self.data == value: return True
        
        if value < self.data:
            # value might be in the left subtree
            if self.left:
                return self.left.search(value)
            else:
                # reach a end
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                # reach bottom
                return False
    
    def find_min(self,root):
        # it must be at the left end
        current = root.left
        
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self,root):
        # it must the the rightmost leaf node
        # 和单链表一样，加个probe来traverse向前走
        current = root.right
        while current.right:
            current = current.right
        
        return current.data
                
    def calculate_sum(self,root):
        # just need to traverse once and grab the value
        return sum(self.in_order_traversal(root))
    

                   
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
        
if __name__ == "__main__":
    elements = [17,4,1,20,9,23,18,34]
    
    root_node = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root_node.add_child(elements[i])

    print(root_node.in_order_traversal(root_node))
    print(root_node.pre_order_traversal(root_node))
    print(root_node.post_order_traversal(root_node))
    print(root_node.find_min(root_node))
    print(root_node.calculate_sum(root_node.left))