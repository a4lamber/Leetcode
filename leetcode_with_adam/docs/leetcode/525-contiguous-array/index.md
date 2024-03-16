---
tags:
    - Prefix Sum
    - Hash Table
    - Array
---

# 525 Contiguous Array



## Approach 1 Prefix Sum + Hash Table

prefix sum + hash table擅长解决subarray sum == target的问题, 但这一题则有点不一样, 给的binary array, 我们需要找到最长的subarray, 使得0和1的数量相等. 要用到一个trick, 把所有的0转化为-1，这样这个问题就等价于找到最长的subarray sum == 0, 如下例子

```python
# 原数组
[0, 1, 0, 1, 0, 1]
# 转化后的数组
[-1, 1, -1, 1, -1, 1]
```
这样就能把这个问题转化为最长的subarray sum == 0的问题了, 然后我们需要用到一个概念就是任何一个subarray的sum都可以由其它两个subarray的sum相减得到, 如下公式

```
sum[j:i] => prefix_sum[i] - prefix_sum[j-1]
case 1:
-------------------
x x x [x x x]
   j-1 j   i
case 2 (edge case):
-------------------
  [x x x] x x x
-1 0 1 i
```
但还有一个edge case, 就是以0为起点的subarray, 并没有j-1, 所以我们需要在hash table里面初始化一个prefix_sum[0] = -1, 这样就能cover这个edge case了. 


### Code Implementation

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashtable = dict()
        hashtable[0] = -1
        
        prefix_sum = 0
        res = 0
        for i,num in enumerate(nums):
            if num == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            if prefix_sum in hashtable:
                res = max(res,i - hashtable[prefix_sum])
            else:
                hashtable[prefix_sum] = i
        
        return res            
```


## Reference

- [wisdom peak LC 525 Contiguous Array](https://www.youtube.com/watch?v=uYuSLvjEyjQ)