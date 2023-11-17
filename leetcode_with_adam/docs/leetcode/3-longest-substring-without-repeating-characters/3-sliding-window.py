class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window (dynamic) using hashset
        left = 0
        res = 0
        hashSet = set()

        for right in range(len(s)):
            # 判断新的char是否在hashset之中, O(1)
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            # 假设这个string没有任何重复的，会这么写
            hashSet.add(s[right]) # 加入新的char
            
            # 比较当前sliding window大小和以前的最大长度打擂台
            if right - left + 1 > res:
                res = right - left + 1
        
        return res
