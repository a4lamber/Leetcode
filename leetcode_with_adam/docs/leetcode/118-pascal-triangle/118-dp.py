class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 杨辉三角形 binomial coeffient 类型;

        # edge cases
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]

        # recurrence cases
        triangle = [[1],[1,1]]
        # starting from row 3
        for i in range(3,numRows+1): # +1 是因为right hand exclusive in python
            # initialze the array of size 
            row = [None] * i # 每一行都有rownumber数量的elements
            
            # add the 1st element
            row[0] = 1
            for j in range(1,i-1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            
            # add the last element
            row[i-1] = 1

            # append to the result list
            triangle.append(row)  

        return triangle
