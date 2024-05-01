---
tags:
    - Hash Table
    - String
    - Bit Manipulation
    - Prefix Sum
---

# 1915 Number of Wonderful Substrings

几点问题，

- 如何能想到要用 bit shift + exclusive or (XOR) 来解决问题？

## Approach 1: Prefix + Hash + Bit

odd frequency of letter appear at most 1, 可以被分解为两个子问题:

- 求ending at char i的substring中，有多少个odd letter出现0次
- 求ending at char i的substring中，有多少个odd letter出现1次

### 描述状态

为了更好的描述state, 我们可以用:

- letter出现过odd次, bit为0
- letter出现过even次, bit为1

每当我们substring长大时，我们可以用`flip k-th bit`来作为状态转移方程来迭代，`mask ^= (1 << k)`, 也就是说我们可以用一个10位的mask来表示当前的状态，比如:

```
a (1 << 0)
b (1 << 1)
c (1 << 2)
d (1 << 3)
e (1 << 4)
f (1 << 5)
g (1 << 6)
h (1 << 7)
i (1 << 8)
j (1 << 9)
```

假设`s=''`, 初始值为`0000000000`, 你可以把它理解为每个char都只出现了偶数次. 每遇到一个新的char, 我们就flip对应的bit with XOR. 我们来做一下dry run, for substring `'acadac'`

|substring|mask|
|-|-|
|`''`|0|
|`'a'`|1|
|`'ac'`|101|
|`'aca'`|100|
|`'acad'`|1100|
|`'acada'`|1101|
|`'acadac'`|1001|

接下来我们只需要维护一个hasmap作为我们的prefix即可,

```json
{
    0: 1,
    1: 1,
    101: 1,
    100: 1,
    1100: 1,
    1101: 1,
    1001: 1
}
```

### 子问题1: odd letter出现0次

我们只需要记录当前的mask, 看之前是否出现过，出现过几次就可以这个解的可能性. 维护一个frequency map即可

### 子问题2: odd letter出现1次

flip `k-th` bit, 然后看之前是否出现过，O(10)

!!! note
    
    - Time Complexity: $O(n)$
    - Space Complexity: $O(n)$, worst case scenario 10个解

### Code Implementation

```python
from collections import defaultdict
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        case 1: odd freq出现0次
        case 1: odd freq出现1次
        表示state:
            jihgfedcba
        
        a --> 2^0 --> 1
        b --> 2^1 --> 2
        ...
        """
        # initialize a frequency map
        freq = defaultdict(int)
        freq[0] = 1

        mask = res = 0

        for char in word:
            bit = ord(char) - ord('a')
            # flip current char's bit to get flip mask
            mask ^= (1 << bit)

            # case 1: no letter appearing odd number of times
            res += freq[mask]
            freq[mask] += 1

            # case 2: one letter appearing odd number of times
            for odd_char in range(0,10):
                curr = mask ^ (1 << odd_char)
                if curr in freq:
                    res += freq[curr]
        return res
```