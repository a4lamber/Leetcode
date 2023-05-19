def mergeSort(array):
    """
    Implementation of mergeSort. Key to understand this is by looking at
    call stack for this function
    
    Reference:
    https://www.youtube.com/watch?v=4acikH5mXwk
    Args:
        array (_type_): _description_

    Returns:
        _type_: _description_
    """
    # when still divisible
    if len(array) > 1:
        
        # half of the index
        mid_index = len(array)//2
        L = array[:mid_index]
        R = array[mid_index:]
        
        # Sort the two halves
        mergeSort(L)
        mergeSort(R)
        
        # initialize three counter
        # i for index in sub-array L
        # j for index in sub-array R
        # k for index of the sorted array
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        
        #     
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1 
        
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
            

    return array

if __name__ == "__main__":
    test = [1,3,4,2,5,7,1,0,2,3]
    
    print("Sorted by selection sort in ascending order:")
    a = mergeSort(test)
    print(a)
            
        
        