class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # step1. permutation
        # step2. palindrome

        # craete a hashtable and count frequencies
        hashtable = {}
        for char in s:
            if char not in hashtable.keys():
                hashtable[char] = 1
            else:
                hashtable[char] += 1
            
        # 两种conditions是palindrom的条件:
        # odd number of string, 其中有一个x%2 == 1, 剩下的都满足y%2 == 0
        # even number of string, 那么每个item都满足y%%2 == 0:
        if len(s) % 2 == 0:
            # 先看偶数case
            for key,value in hashtable.items():
                if value % 2 != 0:
                    return False
        else:
            # 再看奇数case
            pointer = 0
            for key,value in hashtable.items():
                if value%2 == 1:
                    pointer += 1
        
            if pointer > 1:
                return False
                    
        return True
