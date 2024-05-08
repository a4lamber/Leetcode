class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse integer approach
        # edge cases: 0, 120 and all negative number
        # 技巧是如何reverse int number, 计算个位的数字, 然后流入reversed number
        # 原有的数不断floor division by 10 来降位, reversed number不断乘以10来升位

        if x < 0 or (x%10 == 0 and x!=0):
            return False

        
        original_num = x
        reversed_num = 0

        # 只要x不在0-9, 都会大于0
        while x > 0:
            # 计算个位数，然后从另一头流入reversed_num
            digit = x%10

            # reversed number不断升位
            reversed_num = reversed_num * 10 + digit
            
            # floor division to get rid of it
            x = x//10
        
        return original_num == reversed_num


        

        


            
            