def bubbleSort(array):
    """
    Implementation of bubble sort in python in ascending order.
    每一个外循环,把一个最大的数，移到最右边.
    每一个内循环,比较相邻的两个数，如果左>右，则换.
    Args:
        array (_type_): unsorted array

    Returns:
        _type_: sorted list
    """
    count = len(array)
    
    # _ if u r not interested in using the index to do anything and want to 
    # avoid unused variable, you use underscore
    for _ in range(len(array)):
        count -= 1
        for j in range(count):
            # compare adjacent elements, if left > right then good
            if array[j] > array[j+1]:
                # notorious python in-line swap
                array[j],array[j+1] = array[j+1],array[j]

    return array



def bubbleSortOpt(array):
    """
    slight optimization to determine whether the array is sorted, if sorted, no need
    to do redundant work.
    Args:
        array (_type_): unsorted array

    Returns:
        _type_: _sorted list
    """
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - 1 - i):
            # compare adjacent elements, if left > right then good
            if array[j] > array[j+1]:
                # notorious python in-line swap
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        # if swapped = False at the end of iteration, it means array is sorted
        # so just break the loop
        if not swapped:
            break
    return array




test = [1,3,4,2,5,7,1,0,2,3]


a = bubbleSort(test)
b = bubbleSortOpt(test)
print(a)
print(b)

