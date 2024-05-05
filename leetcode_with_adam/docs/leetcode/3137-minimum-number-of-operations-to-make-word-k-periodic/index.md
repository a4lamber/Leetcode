# [3137 Minimum Number of Operations to Make Word K-Periodic](https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/)

## Approach 1

有一个数组，可以分为`n//k`个segment, 每个segment的长度为k，我们可以用一个hashtable来记录每个segment的出现次数，然后找到出现次数最多的segment. 这个就是不动的segment,其它的segment都需要被替换。

For example, `word = leetcodeleet` and `k = 4`, 可以分为`leet`, `code`, `leet`三个segment, 统计一下,
```json
{
    "leet": 2,
    "code": 1
}
```

由此我们可以看到，`leet`出现了两次，最划算的operation时只需要替换一次就可以了。

!!! note '复杂度分析'

    - time complexity: $O(\frac{n}{k})$
    - space complexity: $O(\frac{n}{k})$


### Code Implementation

```python
from collections import defaultdict
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        """
         1.  4.  8
        [leetcodelee t ]
         01234567891011
         we replace
         - [0..3] with [4..7]
         - [4..7] with [8..11]
          
          0 2 4 6 8
         [leetcoleet]
          0123456789
        
        example 1分成3等份
        example 2分成5等份
        只有最后一个segment不能被替换，所以我们可以利用count次数来决定
        """
        n = len(word)
        # target = word[n-k:n]
        hashtable = defaultdict(int)
        
        global_max = 0
        for i in range(n//k):
            start = i*k
            end = (i+1)*k
            hashtable[word[start:end]] += 1
            global_max = max(global_max,hashtable[word[start:end]])

        return n//k - global_max
```