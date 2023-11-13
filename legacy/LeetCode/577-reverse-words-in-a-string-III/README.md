# Approach1: 瞎写的
<!-- Describe your approach to solving the problem. -->
自己写的，挺凌乱的，这里要注意以下几点:

- `python`不支持string assignment, 所以用two pointer method做string in-place swap不行，还是只能append到list中

这一题还是要以后用别的语言写一遍，才能更理解吧.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```python
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

        
            
```