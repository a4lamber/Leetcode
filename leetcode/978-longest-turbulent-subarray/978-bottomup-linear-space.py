class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # DP[i]: length of maximum turbulent subarray ending on arr[i]
        # bottomUp constant space Solution

        if len(arr) == 1: return 1
        # initialize DP, at first two elements
        DP = [None for _ in range(len(arr))]
        DP[0] = 1        
        if arr[0] == arr[1]:
            DP[1] = 1
        else:
            DP[1] = 2

        # bollean flag
        flag = arr[1] > arr[0]


        for i in range(2,len(arr)):
            # edge case when equal, we reset to 1
            if arr[i] == arr[i-1]:
                DP[i] = 1
                continue

            if flag ^ (arr[i] > arr[i-1]):
                # successfully update
                DP[i] = DP[i-1] + 1

                # update flag
                flag = arr[i] > arr[i-1]
            else:
                # update fails, rest to maximum turbulent subarray length ending on arr[i], which is 2.
                DP[i] = 2

        return max(DP)

