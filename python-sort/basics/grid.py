'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2022-09-05 16:29:52
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2022-09-05 18:21:21
 # @ Description: implementation of Grid class by nesting array with array.
 '''

# read the Array class we just created
from array import Array

class Grid():
    """
    Grid class is essentially a two-dimensional array.
    """
    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows)
        for i in range(rows):
            # assign each memory cell in an Array with another array
            self.data[i] = Array(columns, fillValue)

    def getHeight(self):
        """
        returns the # of rows. During initialization, an Array() is a 1D linear collection 
        """
        return len(self.data)
    
    def getWidth(self):
        """returns the # of columns. 第一个Array中，每一个index插入的都是一样的"""
        return len(self.data[0])
    
    def __getitem__(self,index):
        """
        allowing access from index.
        accessing an element: [i][j]
        accessing an column: [i] 
        """
        return self.data[index]
    
    def __str__(self):
        """Returns a string representation of the grid"""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result


if __name__ == "__main__":
    a = Grid(10,12)
    print(a)

