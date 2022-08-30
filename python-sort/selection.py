def selectionSort(array):
    """
    Sort an array in ascending order with selection sort.
    算法开始前，假设第一个element为最小.
    每一个外循环, 寻找出整体最小值，用打擂台的方法.
    每一个内循环，比较当前值a和整体最小值min, 如果a<min, min = a
    Args:
        array (_type_): unsorted array

    Returns:
        _type_: sorted array in ascending order.
    """
    for i in range(0,len(array),1):
        # Before sorting, assuming 1st element in unsorted array is smallest
        min_index = i
        
        for j in range(i+1,len(array),1):
            # compare current value with min value in unsorted array
            if array[j] < array[min_index]:
                min_index = j
        # swap the min to the beginning of the array
        array[i],array[min_index] =  array[min_index],array[i]
    
    return array
            



test = [1,3,4,2,5,7,1,0,2,3]
print("Sorted by selection sort in ascending order:")
a = selectionSort(test)
print(a)