class Solution:
    def firstUniqChar(self, s: str) -> int:

        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap.keys():
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1

        for i in range(len(s)):
            if s[i] in hashmap.keys() and hashmap[s[i]] == 1:
                return i

        return -1
