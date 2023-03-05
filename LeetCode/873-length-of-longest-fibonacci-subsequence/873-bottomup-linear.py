class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP[i][j]: length of longest fibonacci subsequence ending on arr[i], arr[j]
        # for example: arr = [1,3,7,11,12,14,18], DP[3][4] = 3; [1,11,12] = 
[arr[0],arr[3],arr[4]]
        # constant space Solution
        
        fib_hash = {}

        # create a hash for look up
        for i in range(len(arr)):
            fib_hash[arr[i]] = i
        
        # initialze 2D array
        DP = [[2 for _ in range(len(arr))] for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                target = arr[j] - arr[i] # k增加,arr[k]增加,target单调递增
                # target < arr[i] < arr[j]
                if target < arr[i] and target in fib_hash:
                    k = fib_hash[target]
                    DP[i][j] = DP[k][i] + 1
        
        ans = max([max(value) for value in DP])

        return ans if ans >= 3 else 0
        

        
        
        
        
        

