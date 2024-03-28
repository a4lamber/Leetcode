class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # we could reduce the problem to LCS problem, then we operate
        # the length is 10^4, if using 2D DP approach, it would be O(10^8)
        x = len(s)
        y = len(t)

        LCS = [[0]*(y+1) for _ in range(x+1)]

        for i in range(x+1):
            LCS[i][0] = i
        
        for j in range(y+1):
            LCS[0][j] = j

        
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s[i-1] == t[j-1]:
                    LCS[i][j] = LCS[i-1][j-1]
                else:
                    # number of operations needed just increase by one
                    LCS[i][j] = 1 + min(LCS[i-1][j],LCS[i][j-1],LCS[i-1][j-1])
            
        return LCS[-1][-1] == 1
