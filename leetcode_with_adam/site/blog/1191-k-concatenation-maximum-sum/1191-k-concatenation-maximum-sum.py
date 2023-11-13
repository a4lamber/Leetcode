class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # Note: reduce the problem to maximum subarray
        # maximum prefix sum, maximum suffix sum
        def kadane(dummy_array):
            if len(dummy_array) == 1: return max(dummy_array[0],0)
        
            current_max = max(dummy_array[0],0)
            global_max = max(dummy_array[0],0)

            for i in range(1,len(dummy_array)):
                # 由于这题支持len(subarray) == 1, 所以
                current_max = max(current_max + dummy_array[i], dummy_array[i])
                if current_max > global_max: global_max = current_max

            return max(global_max,0)

        mod = 10**9 + 7
        # 排除所有k = 1的case
        if k == 1:
            return (kadane(arr)) % mod
        # 只剩下k >= 2
        if sum(arr) > 0:
            return (kadane(arr+arr) + (k-2) * sum(arr)) % mod
        else:
            return (kadane(arr+arr)) % mod

        

                
            


            
        
