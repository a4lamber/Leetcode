def insertion_sort(A):
    for i in range(1,len(A)):
        # 需要被sort的数
        key = A[i]
        # 向左需要循环的次数
        j = i - 1
        # 跳出循环两个条件, 碰到大于key的数字了 and j != -1
        while j >= 0 and A[j] > key:
            # shuffle everything to the right by one
            A[j+1] = A[j] 
            # move to left by one 
            j = j - 1
        
        # insert the value 
        A[j+1] = key
    
    return A
        

test = [2,4,10,1,7,10]        
print(insertion_sort(test))