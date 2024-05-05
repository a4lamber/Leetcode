# [3138 Minimum Length of Anagram Concatenation](https://leetcode.com/problems/minimum-length-of-anagram-concatenation/description/)


## Approach 1 

找规律，比赛的时候我发现,

- 先维护一个frequency map for each char `count = Counter(s)`, 再求最小frequency的char, `min_freq`
- edge case:
    - 如果只有一个char, 那么直接返回1
- general cases:
    - 如果最小的频率为1, 那么必然只能构成一个anagram, 返回len(s)
    - 如果最小的频率大于1, 分类讨论:
        - 所有的数都能被最小的频率整除, 那么直接返回最小的频率
        - 不能被整除, 那么返回len(s)

代码实现如下,

```python
from collections import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        """
        observation:
        - O(n) solution or at worst O(nlogn)
        - "xxe"
        - "" --> "bboorruull"
        - "" --> "ooooiinnss", 还存在某些偶数的情况;
        """
        count = Counter(s)       
        # 只有一个char
        if len(count) == 1:
            return list(count.values())[0]
        
        # 获得最小值
        min_freq = min(count.values())
        distinct_freq = sorted(set(count.values()))
        
        # 如果min_greq为1，那么不管其他值是多少,都必然是n
        if min_freq == 1:
            return len(s)
        
        for freq in distinct_freq:
            if freq % min_freq != 0:
                return len(s)
        
        return min_freq
```

但有几个hidden test cases没法跑过，所以这个逻辑还是不够全面。没cover到的test cases的`distinct_freq`为

```
distinct_freq = {385, 322, 420, 357, 294, 329, 427, 364, 301, 399, 336, 371, 308, 406, 343, 441, 413}
min_freq = 294
```
原因在于我比赛中想到的是"所有的数能被最小的frequency整除", 但这个不够全面。最全面的是，`找到一个最大数字x, such that所有的char的频率都能被x整除`. 这个x就能满足我们最短anagram长度.


### Code Implementation

```python
from collections import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        """
        observation:
        - O(n) solution or at worst O(nlogn)
        - "xxe"
        - "" --> "bboorruull"
        - "" --> "ooooiinnss", 还存在某些偶数的情况;
        
        最后的solution的freq, 必然是:
        - 如果freq map只有一个char, 那就是1
        - 只要存在1, 那么必然是len(s)
        - 最后的char, freq map, 必然是, 
        https://oi-wiki.org/math/number-theory/gcd/
        """        
        count = Counter(s)       
        com_div = count[s[0]]

        for count in count.values():
            com_div = math.gcd(com_div,count)
        return len(s)//com_div
```