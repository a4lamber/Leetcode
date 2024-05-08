class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1: removing all non-alphanumerical chars and convert upper to lower cases
        
        clean_s = ""

        # get the alphanumerical char into the clean_s
        for char in s:
            if char.isalnum():
                clean_s += char
            else:
                # it's not
                continue

        # convert it all to lower cases
        clean_s = clean_s.lower()

        head = 0
        tail = len(clean_s) - 1

        # two pointer, opposite direction problem
        res = False
        while tail > head:
            # check 
            if clean_s[head] != clean_s[tail]:
                return res
            # advance two pointers by one
            head += 1
            tail -= 1

        res = True
        return True



        



        
        