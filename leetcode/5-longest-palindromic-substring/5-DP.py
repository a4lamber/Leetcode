class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP[i][j]: longest palindromic substring 
        n = len(s)
        # initialize
        DP = [[False]*n for _ in range(n)]
        for i in range(n):
            DP[i][i] = True

        longest_palindrome_len = 1
        longest_palindrome_start = 0

        # constrain start < end; 
        for end in range(n):
            for start in range(n,-1,-1):
        # for end in range(n):
        #     for start in range(end-1,-1,-1):
                if end > start and s[start] == s[end]:
                    if end - start == 1 or DP[start+1][end-1]:
                        DP[start][end] = True
                        curr_palindrome_len = end - start + 1
                        # check if we need to update
                        if longest_palindrome_len < curr_palindrome_len:
                            longest_palindrome_len = curr_palindrome_len
                            longest_palindrome_start = start
        
        return s[longest_palindrome_start:longest_palindrome_start+longest_palindrome_len]

                    
                    



        
