class Solution:
    def isValid(self, s: str) -> bool:
        # use list to emulate array-based stack
        stack = []

        # a hash with closing bracket as keys and opening bracket as value
        mapping = {
                    "}":"{",
                    "]":"[",
                    ")":"("    
                  }

        # traverse every element in the string
        for char in s:
            if char in mapping.keys():
                # 这个字符是closing bracket
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "dummy"
                
                if mapping[char] != top_element:
                    # 错位了,对不上号 
                    return False
            else:
                # 这个字符是opening bracket
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
        