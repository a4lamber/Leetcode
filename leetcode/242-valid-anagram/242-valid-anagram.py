class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # hash储存key-value pair 
        # key: every distinct char
        # value: 该char在string中出现的总次数
        hashtable = {}

        # iterate through string s 
        for i in range(len(s)):
            # 判断该char是否在里面, 如果在，累加一次
            if s[i] in hashtable.keys():
                hashtable[s[i]] += 1
            else:
                # 该char第一次出现
                hashtable[s[i]] = 1

        for j in range(len(t)):
            if t[j] in hashtable.keys():
                hashtable[t[j]] -= 1
            else:
                # 在string t中发现了new char, 不是anagram
                return False

        # 
        for item in hashtable:
            # 如果有哪一个value, 不是0, 则说明多出现了或者少出现了一次
            if hashtable[item] != 0:
                return False

        return True