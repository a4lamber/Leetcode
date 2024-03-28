class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # DP[i,j]: maximum length of repeated subarray ending on nums1[i] and nums2[j]

        m = len(nums1)
        n = len(nums2)
        
        last_row = [0 for _ in range(n+1)]
        DP = [0 for _ in range(n+1)]
        max_length = 0
        

        # left right scan
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    # 相等,info from the top left
                    DP[j] = last_row[j-1] + 1
                else:
                    DP[j] = 0
                # update max_length
                max_length = max(DP[j],max_length)

            # update it
            last_row = DP.copy()
        
        return max_length