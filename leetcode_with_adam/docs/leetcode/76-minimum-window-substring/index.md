# Approach 1 Sliding Window

很classic的sliding window的题目. 首先看constraints,
- `- 1 <= s.length, t.length <= 10^5`

由此可以推断出，这个题目的时间复杂度是`O(n)`，至多是`O(nlogn)`.

因此我们把重心放在如何构建sliding window和左右指针的移动上，必须保证构建方法能traverse整个s efficiently. Recall two sum,这些题目都是用hashmap来解决的. 我们可以用两个hashmap来记录
- 我们需要的`need_hash`
- 我们拥有的`have_hash`

如下图所示
```
have_hash               need_hash
key  value              key  value
A       1               A       1
B       1               B       1
D       1               C       1
E       1               
O       1
```
!!! tip Tip
    用hashmap的原因是，我们需要执行find的操作，在array里面，find的时间复杂度是`O(n)`，而在hashmap里面是`O(1)`.

我们`right`不断遍历前进，每次遍历都会更新`have_hash`，然后可以比较need_hash和have_hash的情况，如果满足条件，我们就可以开始更新`left`指针了. 但这里我们可以用两个变量`need`和`have`来记录我们满足的条件， 不然每次`right++`, 我们都需要比较两个hashmap的情况，`O(len(need_hash))`的时间复杂度. 


这题让我卡住的点在于左指针的更新，有以下两点:
- `左指针不需要back track:` 按照我原来的思路，每次`right++`



## Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(s) < len(t): return ""

        # construct two hashmap to record what we need and have
        need_hash = collections.defaultdict(int)
        for char in t:
            need_hash[char] += 1

        have_hash = collections.defaultdict(int)

        # two integers to record how many conditions we have met so far
        need,have = len(need_hash),0
        
        res,res_len = (-1,-1),float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            have_hash[c] += 1

            if c in need_hash and have_hash[c] == need_hash[c]:
                have += 1
            
            # 开始更新左指针
            while have == need:
                # update our result if current window_size < res_len
                if (right - left + 1) < res_len:
                    res = (left, right)
                    res_len = right - left + 1
                # pop from the left of our window
                have_hash[s[left]] -= 1
                # update hash count
                if s[left] in need_hash and have_hash[s[left]] < need_hash[s[left]]:
                    have -= 1
                # back track
                left += 1

        left,right = res
        return s[left:right+1] if res_len != float("infinity") else ""
```

## Complexity Analysis

|-|time complexity|space complexity|
|-|-|-|
|-|`O(n)`|`O(1)`|
