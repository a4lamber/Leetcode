class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # recursive solution, in-place and return nothing
        # 注意，这是不用return的情况, 因为题目的function header output为None 

        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                # recursively call helper
                helper(left+1,right-1)
        
        # let the recursion begin!
        helper(0,len(s)-1)