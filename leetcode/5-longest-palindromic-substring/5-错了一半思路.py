def isPalindrome(s):
    # read in a string, returns boolean for whether it's palindrome or not
    left,right = 0,len(s) -1
    
    while left < right:
        if s[left] != s[right]:
            return False 
    
        left += 1
        right -= 1

    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointer approach
        # the right pointer keeps moving until it matches s[left]
        # then it starts to determine whether it's a palindromic substring
        # then record it to longest 

        # edge case, only one char or only one repeating character
        if len(s) == 1 or len(set(s)) == 1:
            return s[0]

        left,right = 0,1
        longestSubstring = ""

        while left < len(s):
            # 判断如果right pointer到end也没有，则left += 1, rest right
            if right == len(s):
                left += 1
                right = left + 1
                continue

            # 如果left and right指针对应的char一样
            if s[left] == s[right]:
                if isPalindrome(s[left:right+1]):
                    # 判断是否是palindrome
                    if len(s[left:right+1]) > len(longestSubstring):
                        # it's palindrome, 右指针继续移动
                        longestSubstring = s[left:right+1]
                    
            
            # keeps moving right pointer
            right += 1

        return longestSubstring









            