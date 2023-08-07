class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start,curr):
            # base case
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            # 只看右边的解，right hand exclusive in python
            for i in range(start,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()

        # starting from 1
        backtrack(1,[])
        return res 
