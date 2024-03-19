---
tags:
  - Array
  - Hash Table
  - Prefix Sum
---

# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)

这题几个思路:

- brute force O(n^3). O(n^2) for traversing all subarraies, O(n) for sum
- preprocessing prefix sum O(n) and traversal all subarraies O(n^2).
- 利用two sum的思想，hashtable + prefix sum O(n) for time and space. 最优解.


## Approach 1: Prefix Sum + Hash Table

Hash + prefix sum解法，思路有点像two sum, 由于是求两者之和等于target的题目，这一题有意思的是prefix sum的解法, 思路是这样的，如果你计算accumulative sum, 你可以这样做, 

![](./assets/image-lc560.png)


pre-fix sum基于的理论是:

- 任何一个sub-array, 都可以由two sub-array的差值来构建出来.


迭代到在任何一个时间点`i`的prefixSum的值，在删去一些前缀array之后，能组合成任何一个以`nums[i]` 为结尾的subarray, 这样你只要iterate one pass, 就能考虑到所有subarray的情况;

其实很像数轴标根穿针引线法的思路，当你前面满足了x个particular sum等于某个数的时候，就相当于多了x种可能性.

![](https://img-blog.csdnimg.cn/img_convert/3dc9883d13dc036b836745adf1adb0f1.png)

```python
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        x x x [x x x x]
               j     i
        sum[j..i] = prefix[i] - prefix[j-1]
        """
        hashtable = defaultdict(int)
        hashtable[0] = 1

        total = 0
        prefix = 0
        for i,num in enumerate(nums):
            prefix += num
            target = prefix - k
            if target in hashtable:
                total += hashtable[target]
            # add the current prefix frequency by 1            
            hashtable[prefix] += 1
        
        return total
```

这题思路的进阶2D版是[1074 Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/?envType=daily-question&envId=2024-01-28)

