class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = valley = 0

        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                peak += 1
            
            if arr[i-1] >= arr[i] <= arr[i+1]:
                # plateau, valley, left hill + plateau, plateau + right hill
                valley += 1

        return peak == 1 and valley == 0
            

            
