---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Problem 
Longest substring without repeating characters. Given a string `s`, find the length of the longest substring without repeating characters.

### Example1
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example2
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example3
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```


# Algorithm

## Brute force
这一题思路如下, 第一个思路是，traverse all string, 然后打擂台只保留length of longest string, $O(n^2)$ 遍历所有string, 你还得写一个helper function来判断是否有duplicate比如:

```python
def helper(substring):
    if len(substring) == len(set(substring)): return True
    return False
```
由于[convert a list/string to hashset](https://stackoverflow.com/questions/34642155/what-is-time-complexity-of-a-list-to-set-conversion):
- iterating over a list is `O(n)`
- adding each element to hashset`O(1)`

So helper function has $O(n)$, so brute force would be $O(n^3)$

This is way we need sliding window technique


## Sliding window 

Sliding window problem 有以下几个条件要判断作为framework:

- 选什么DS做window?
  - sliding windowing, 可以选用`list()`或者`set()`来做这件事情，但是由于我们需要判断一个character是否是duplicate inside a string，如果用list作为sliding window, 要做linear search O(n), 然而hashset 为 O(1) `if key in hashSet:`, 所以我们用`set()`.
- 什么做window的boundary
  - left and right pointer (sliding window可以说是双指针法的variation)
- 最简单的case是什么?怎么implement?
  - simpliest case `s = sijgopq` non-repeating character. 也就是你的sliding window的右边界(right) traverse the string. 每一步都add s[r] into the hashset. 同时你比较一下现在window的长度和上一个时步的window长度即可;
  - ```python    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # slding window (dynamic) using hashset
        left = 0
        res = 0
        hashSet = set()

        for right in range(len(s)):
            # 假设这个string没有任何重复的，会这么写
            hashSet.add(s[right]) # 加入新的char
            
            # 比较当前sliding window大小和以前的最大长度打擂台
            if right - left + 1 > res:
                res = right - left + 1
        
        return res
   
- 我加什么条件可以从simplest case扩展到general case.
  - 这一步也是精髓，`while s[right] in hashSet`, pop左指针指向的current substring最左边的element, 然后左指针进一位，再继续判定`s[right] in hashSet`




# Code
```python
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
```