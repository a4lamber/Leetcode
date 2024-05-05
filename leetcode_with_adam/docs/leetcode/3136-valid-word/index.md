# [3136 Valid Word](https://leetcode.com/problems/valid-word/)

没啥特别的，就是检查一个字符串是否满足以下条件：

```python
class Solution:
    def isValid(self, word: str) -> bool:
        # It contains a minimum of 3 characters.
        # It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
        # It includes at least one vowel.
        # It includes at least one consonant.
        """
        0-9, 48-57
        A-Z, 65-90
        a-z, 97-122        
        """
        if len(word) < 3:
            return False
        
        vowels = set('aeiouAEIOU')
        numbers = set('0123456789')
        vowel_flag = False
        consonant_flag = False
        
        for char in word:
            curr = ord(char)
            # not a number, lower case, upper case, and special chars
            if curr < 48 or (curr > 57 and curr < 65) or (curr > 90 and curr < 97) or curr > 122:
                return False
            
            if char in vowels:
                vowel_flag = True
                continue
            
            if char not in vowels and char not in numbers:
                consonant_flag = True
        
        if vowel_flag and consonant_flag:
            return True
        else:
            return False
```