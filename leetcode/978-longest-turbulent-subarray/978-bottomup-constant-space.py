class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # bottom up, constant space
        # current_length: current maximum turbulent ending on

        if len(arr) == 1: return 1

        # initialize DP, at first two elements
        if arr[1] == arr[0]:
            current_length = 1
        else:
            current_length = 2

        maximum_length = current_length

        # bollean flag
        flag = arr[1] > arr[0]

        for i in range(2,len(arr)):
            # edge case when equal, we reset to 1
            if arr[i] == arr[i-1]:
                current_length = 1
                maximum_length = max(maximum_length,current_length)
                continue

            if flag ^ (arr[i] > arr[i-1]):
                # turbulent, so increment current length
                current_length += 1
                # update flag
                flag = arr[i] > arr[i-1]
            else:
                # rest current_length to 2, which only has two elements [0,1,2] --> [1,2] 
                current_length = 2
            
            maximum_length = max(maximum_length,current_length)

        return maximum_length






