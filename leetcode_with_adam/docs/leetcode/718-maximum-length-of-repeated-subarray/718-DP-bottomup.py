class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # DP[i,j]: maximum length of list ending on nums1[i] and nums2[j]

        m = len(nums1)
        n = len(nums2)

        DP = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    # 相等,info from the top
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    # 既然俩array, last element不等，那么它们必然不share repeating array ending on nums1[i] and num2s[j]
                    DP[i][j] = 0
        
        return max(max(row) for row in DP)

