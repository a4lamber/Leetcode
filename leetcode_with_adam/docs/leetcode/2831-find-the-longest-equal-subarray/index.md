---
tags:
    - Array
    - Sliding Window
    - Hash Table
---

# 2831 Find the longest equal subarray

深度好题，删除至多k个元素，使得subarray中的元素相等，求最长的符合条件的subarray长度.

## Approach 1: Sliding Window (O(n) in time & space)

equal subarray一定符合其中所有元素都相同like [A A A A A A]. 既然如此，那么首尾必然也相同，都是A. 那么根据这个，我们看以下的数组，

```
0. 1.2 3 4 5 6  7 8 9 10 11 12
X [A X X A X A] X X X A  X  X
   i         j
```
因此，我们可以花费O(n)的空间构造一个hash map, 记录每一个不同元素出现过的indices.

```json
{
    "A" : [1, 4, 6, 10],
    "X" : ....
}
```
然后我们遍历其中每一个space即可, 

```
 0 1 2  3
[1,4,6,10]

total # elements - #A
(4 - 1 + 1) - (1 - 0 + 1) > k
```

Algorithm:

- one pass to create such hashmap
- iterate all items() in the hashmap where len() >= 2.
    - initialize left,right = 0,1
    - move left pointer when we need to delete more than k
    - move right pointer when can delete more!

!!! warning
    没想到吧，这个题的时间复杂度还是O(n)的，遍历hashmap时，我们累加起来，其实也只走了一遍，所以是O(n) + O(n) $\approx$ O(n)的. Two pass solution.

```python
from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(list)
        res = 0
        for i,num in enumerate(nums):
            hashmap[num].append(i)
        
        for _,ids in hashmap.items():
            # edge case
            if len(ids) == 1:
                res = max(res,1)
                continue
            left = 0
            for right in range(1,len(ids)):
                if (ids[right] - ids[left] + 1) - (right - left + 1) > k:
                    left += 1
            
            # right out of index by 1
            res = max(res,right - left + 1)
        return res
```

We can cut down some redundant logic,

```python
from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        """
        equal subarray一定符合其中所有元素都相同like [A A A A A A], 
        既然如此，那么首尾必然也相同，都是A. 那么根据这个，我们看以下的数组，
        0. 1.2 3 4 5 6  7 8 9 10 11 12
        X [A X X A X A] X X X A  X  X
           i         j
        因此，我们可以花费O(n)的空间构造一个hash map, 记录每一个不同元素出现过的indices.
        {
            "A" : [1, 4, 6, 10],
            "X" : ....
        }
        然后我们遍历其中每一个space即可, 
         0 1 2 3
        [1,4,6,10]
        total # elements - #A
        (4 - 1 + 1) - (1 - 0 + 1) > k

        Algorithm:
        - one pass to create such hashmap
        - iterate all items() in the hashmap where len() >= 2.
            - initialize left,right = 0,1
            - move left pointer when we need to delete more than k
            - move right pointer when can delete more!
        """
        hashmap = defaultdict(list)
        res = 0
        for i,num in enumerate(nums):
            hashmap[num].append(i)
        
        for ids in hashmap.values():
            left = 0
            for right in range(len(ids)):
                if (ids[right] - ids[left] + 1) - (right - left + 1) > k:
                    left += 1
            
            # right out of index by 1
            res = max(res,right - left + 1)
        return res            
```

## Approach 2: O(n) in time & O(1) in space

Some intuition:

- delete at most k elements from the subarray, 也就是你可以delete up to k elements.
- optimal solution `[num,num,num]` has element `num`. It must be in the element shows up with maximum frequency so far.


我们decompose一下这个问题:

- 找到以index 0为结尾的，里面包含截止到0为止出现最多次数的元素x, 且能够删除至多k个元素
- 找到以index 1为结尾的，里面包含截止到1为止出现最多次数的元素x, 且能够删除至多k个元素
- ...
- 找到以index n-1为结尾的，里面包含截止到n-1为止出现最多次数的元素x, 且能够删除至多k个元素

!!! tip
    `max_freq`的定义为，以0为起点，right为结尾的subarray中出现最多次数的元素的频率. 或者说historical max frequency，并不是目前subarray中的最大频率.


```python
from collections import Counter
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        max_freq = 0
        left = 0
        count = Counter()

        for right,num in enumerate(nums):
            count[num] += 1
            max_freq = max(max_freq,count[num])
            # when 需要删除的数字 >  至多被删除k; too many to delete
            # 移动left pointer, 但为什么只移动一次?
            if right - left + 1 - max_freq > k:
                count[nums[left]] -= 1
                left += 1
        
        return max_freq
```

有几个问题需要解答一下:

- 移动左指针，且update hashmap, 我们减少的元素`nums[left]`难道减少max_freq吗？
    - 无所谓，反正`res = max_freq` at end of the day. Nothing changes.

## 相关题目

According to vlad and lee:

- 2808 minimum seconds to equalize a circular array
- 404 longest repeating character replacement
- 2054 maximize the confusion of an exam

# Reference

- [vlad](https://leetcode.com/problems/find-the-longest-equal-subarray/solutions/3934031/sliding-window-optimization)
- [lee](https://leetcode.com/problems/find-the-longest-equal-subarray/solutions/3934172/java-c-python-one-pass-sliding-window-o-n)
    - [someone explains lee's solution.](https://leetcode.com/problems/find-the-longest-equal-subarray/solutions/3938738/python3-o-n-sliding-window-with-better-explanation-for-the-logic-and-edge-cases)
- [wisdom peak](https://www.youtube.com/watch?v=viTxUBa_Jdo&ab_channel=HuifengGuan)

