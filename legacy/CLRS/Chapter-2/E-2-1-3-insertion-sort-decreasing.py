'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-02-08 22:38:13
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-02-08 22:46:18
 # @ Description: 
 # Exercise2.1-3 use insertion sort to sort array in decreasing order
 '''


def insertion_sort(A,key = 'decreasing'):
    # 假设左1为最大的
    for i in range(1,len(A)):
        # 你现在要sort的牌, 暂时放在place holder里，无家可归了
        key = A[i]
        j = i-1
        
        # 对subarray进行循环
        while j>= 0 and key > A[j]:
            # shuffle to the right
            A[j+1] = A[j]
            j -= 1
        
        # 插入现在在sort的element, 进入subarray中合适的位置
        # 由于上一步 j-= 1,提前往左走了一步,所以这里要加回来;
        A[j+1] = key
    
    return A

test = [31,41,59,26,41,58]
print(insertion_sort(test))    
        
        