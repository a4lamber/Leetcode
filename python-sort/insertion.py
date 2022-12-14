def insertionSort(array):
    """
    sort an array with insertion sort in ascending.
    At the begining of the algorithm, assuming the 1st element is sorted and it's the minimum.
    
    Args:
        array (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(1,len(array)):
        # item as the key
        key = array[i]
        
        # 至多比较次数为j
        j = i - 1
        
        # 循环比较key和sorted portion of the array until max # of comparison reached(placed at zero) 
        # or it's smaller than any array
        # worst case 循环 i 次, best case 1次
        while j >= 0 and key < array[j]:
            # 挪动一下sorted array的顺序
            array[j+1] = array[j]
            # 比较下一组
            j -= 1
        
        # Inser key at place just amller than it
        array[j+1] = key

    return array

test = [1,3,4,2,5,7,1,0,2,3]
print("Sorted by insertion sort in ascending order:")
a = insertionSort(test)
print(a)