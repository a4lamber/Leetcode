class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        last_row_LCS = [0 for _ in range(len(text2)+1)]
        LCS = [0 for _ in range(len(text2)+1)]

        for i in range(1,len(text1) + 1):
            for j in range(1,len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    # info from top left cell
                    LCS[j] = last_row_LCS[j-1] + 1
                else:
                    # info from top or left cell
                    LCS[j] = max(last_row_LCS[j],LCS[j-1])
            # update last row
            for m in range(len(last_row_LCS)):
                last_row_LCS[m] = LCS[m]
        
        return LCS[-1]


