class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointer technique
        head = 0
        tail = len(s) - 1

        while head < tail:
            # python in-line swap
            s[head], s[tail] = s[tail],s[head]
            
            # advances head pointer by one and retreat tail pointer by 1 
            head += 1
            tail -= 1