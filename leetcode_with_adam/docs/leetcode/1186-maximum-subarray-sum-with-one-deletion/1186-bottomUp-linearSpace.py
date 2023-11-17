class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # DP[0][i]: maximum subarray ending on arr[i].
        # DP[1][i]: maximum subarray ending on arr[i], optionally have the right to drop the 
arr[i].

        
        # declare DP and initialization
        DP = [[0 for _ in range(len(arr))] for _ in range(2)]
        DP[0][0] = arr[0]
        DP[1][0] = arr[0]
        

        for i in range(1,len(arr)):
            # kadane'
            DP[0][i] = max(DP[0][i-1] + arr[i], arr[i])
            DP[1][i] = max(DP[1][i-1] + arr[i], arr[i], DP[0][i-1])

        return max(DP[1])


        
        
            
            

        
        

            

        
         

