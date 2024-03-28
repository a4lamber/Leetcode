class Solution:
    def reverseWords(self, s: str) -> str:
        

        whitespace_counter = 0

        # traverse and count # of space, O(n)
        for char in s:
            if char == " ":
                whitespace_counter += 1


        # space complexity, O(n)
        res = []
        
        head = 0
        tail = head


        for i in range(whitespace_counter+1):
            while tail != len(s) -1 and s[tail+1] != " " :
                tail += 1
            
            temp = tail
            # tail the end index of the word     
            
            while tail >= head:
                res.append(s[tail])
                tail -= 1       
            

            if i == whitespace_counter:
                break
            else:
                res.append(" ")
                tail = temp + 2
                head = tail

        return "".join(res)

        
            