class Array(object):
    """
    Define methods: 
    1. dunder method that calls implicitly when activated 
    by certrain keywork such as print(), operators + - > <
    
    2. explicitly call it
    Args:
        object (_type_): _description_
    """
    def __init__(self,capacity, fillValue = None):
        """
        init stands for initialization.
        automatically called __init__ method
        when an instance of the class is created. 
        Args:
            capacity (_type_): size of the array
            fillValue (_type_, optional): initialized value. Defaults to None.
        """
        # list() equivalent to []
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
            
    def __len__(self):
        """Return the length or capacity of the array"""
        return len(self.items)
        
    def __str__(self):
        """String representation of the array. Called implicityly during print()"""
        return str(self.items)
        
    def __iter__(self):
        """
        Supports traversal within a for loop, such as 
        for i in range(10):
            pass
        for item in array:
            pass
        etc
        """
        return iter(self.items)
    
    def __getitem__(self,index):
        """subscript operator for access at index level."""
        return self.items[index]
    
    def __setitem__(self,index,newItem):
        """subscript operator for replacement at index."""
        self.items[index] = newItem


"""
Physical size: number used to initialize the capacity of the array when created.
Logical size: numver of items in the Array that is currently availble.

Physical size vs Logical size:
- if the logical size is 0, the array is empty. That is, the array contains no data item.
- If the logical size equals the physical size, there is no more room for the data in the array. 
"""
