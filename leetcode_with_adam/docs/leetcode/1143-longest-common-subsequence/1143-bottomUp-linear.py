from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS[i,j]: length of LCS with substring text1[0:i] and text2[0:2]
        
        LCS = defaultdict(int)
    
        # horizontal scanning
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    # update from top left corner
                    LCS[(i,j)] = LCS[(i-1,j-1)] + 1
                else:
                    # update from left or top corner
                    LCS[(i,j)] = max(LCS[(i-1,j)],LCS[(i,j-1)])
        
        return LCS[(len(text1),len(text2))]
            
