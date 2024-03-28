from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP[i,j]: the minimum number of operations needed to edit from word1 to word2;
        # base case: 如果任何一个substring为空集，# of ops needed to reach 空集 always will be len(other_words);
        # case 1: if word1[i] == word2[j], then no editing needed from upper left corner
        # case 2: if word1[i] != word2[j], min(top cell, topleft cell, left cell)
        # 由于定义是min # of operations needed, 那么信息可以从任一previous step流动过来


        x = len(word1) 
        y = len(word2)

        # 加入空集的考量，就不用treat边界 and mid nodes different了
        DP = defaultdict(int)

        for i in range(x+1):
            DP[(i,0)] = i
        
        for j in range(y+1):
            DP[(0,j)] = j

        # horizontal scanning, left to right, top to bottom
        for i in range(1,x + 1):
            for j in range(1,y + 1):
                # 判断是否相等
                if word1[i-1] == word2[j-1]:
                    # info is propogating from top left 
                    DP[(i,j)] = DP[(i-1,j-1)]
                else:
                    # info is propogating from top or left
                    DP[(i,j)] = 1 + min(DP[(i-1,j)],DP[(i,j-1)],DP[(i-1,j-1)])

        return DP[(x,y)]

    

        
