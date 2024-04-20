

# 2516 Take K of Each Characters from Left and Right

## Approach 1 Sliding Window

这一题的逻辑是，你需要找到最少操作次数来保证每个字符"a", "b", "c"至少被删除k次，但你的操作只能从左边或者右边开始删除字符. 你可以把这个问题转化from

- minimum number of operations to take at least k of each char "a", "b", "c"

To its equivalent problem

- find the maximum window that satisfies the condition

That's do a dry run with the following example

```
s = "aabaaaacaabc" k = 2
{
    "a": 8,
    "b": 2,
    "c": 2,
}
```

We can subtract k from each character and we get the target

```python
{
    "a": 6, <=6
    "b": 0, <=0
    "c": 0  <=0
}
```

We have our two pointer and 

- if limit has not been reached, we move right pointer
- if limit has been reached, we move left pointer

算法如下:

- edge case: k == 0, return 0
- 设置一个计数器target, 用来记录每个字符的数量, 如果"a","b" or "c"中有一个字符没有出现, 或者减去k之后小于0, 那么直接返回-1
- Initialize 左右指针, 一个计数器和一个窗口大小`window`


```python
from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        target = Counter(s)
        for key in "abc":
            if key not in target:
                return -1
            target[key] -= k
            if target[key] < 0:
                return -1
        
        left = 0
        n = len(s)
        
        count = {char: 0 for char in 'abc'}
        window = 0
        for right in range(n):
            count[s[right]] += 1
            while left <= right and (count['a'] > target['a'] or count['b'] > target['b'] or count['c'] > target['c']):
                # we remove left pointer
                count[s[left]] -= 1
                left += 1
            if left > right:
                # empry-string
                window = max(right-left,window)
            else:
                # non-empty window 
                window = max(right-left+1,window)
            
        return n - window
```

这其中有很多逻辑可以进行优化, 比如:

- 只需要检查`right` pointer刚塞进来的数据即可

```python
from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        target = Counter(s)
        for key in "abc":
            if key not in target:
                return -1
            target[key] -= k
            if target[key] < 0:
                return -1
        
        left = 0
        n = len(s)
        
        count = {char: 0 for char in 'abc'}
        window = 0
        for right in range(n):
            count[s[right]] += 1
            # 只需要考虑刚加进去的即可
            while count[s[right]] > target[s[right]]:
                # we remove left pointer
                count[s[left]] -= 1
                left += 1
            window = max(window,right-left+1)
        return n - window
```