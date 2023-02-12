# 最初代码
<!-- Describe your first thoughts on how to solve this problem. -->
我一开始的代码如下将string进行分类讨论:
- 奇数string, 只有一个字符允许出现奇数次
- 偶数string, 每一个字符出现的frequencies都是偶数次

```python
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
```

# 改良代码
<!-- Describe your approach to solving the problem. -->
借鉴valid parathesis, 可以将上述奇数偶数条件综合一下, 只发现一个unparid element inside the string.

# Complexity
- Time complexity: $O(1)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(2)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 之前的思路:
        # 两种conditions是palindrom的条件:
        # odd number of string, 其中有一个x%2 == 1, 剩下的都满足y%2 == 0
        # even number of string, 那么每个item都满足y%%2 == 0:

        # 利用这个思路，再和valid parathensis中的思路结合一下
        # 奇数和偶数这两个条件的中和条件就是，满足只有一个单身汉,剩下都是情侣

        unpaired = set()

        for char in s:
            if char not in unpaired:
                # 没找到pair, 先去里面等着吧
                unpaired.add(char)
            else:
                # 满足一个pair, 消消乐
                unpaired.remove(char)


        return len(unpaired) <= 1




```