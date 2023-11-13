class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 <= rowIndex <= 33
        # base cases
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]

        prev = [1,1]
        
        for i in range(2,rowIndex+1):
            res = [None] * (i+1)
            # head
            res[0] = 1
            # some sort of in between
            for j in range(1,i):
                res[j] = prev[j-1] + prev[j]
            # tail
            res[i] = 1

            # update prev pointer
            prev = res
        
        return res

