---
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Counting
---

# [992 Subarrays With K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description/?envType=daily-question&envId=2024-03-30)

Sum of the following

- max length of the subarray that ends at index 0 that it's # of uniques == k
- max length of the subarray that ends at index 1 that it's # of uniques == k
...
- max length of the subarray that ends at index n-1 that it's # of uniques == k

Since we want it to be exactly k, so while we are moving left pointer, we must went from having distinct elements in subarray x `x > k` to `x==k` to `x < k`. We can simulate this process


## Approach 1: simulation (TLE)

copy hashmap的cost太高了.

```python
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        observation:
        - good subarray: length of its set == k
        - decompose the problems into a series of subproblems ending at index i
        - sliding window
        Goal:
        Sum of the following
        - max length of the subarray that ends at index 0 that it's # of uniques == k
        - max length of the subarray that ends at index 1 that it's # of uniques == k
        ...
        - max length of the subarray that ends at index n-1 that it's # of uniques == k
        Nope, we want it to be exactly k
        """
        n = len(nums)
        res = 0
        left = 0
        hashmap = defaultdict(int)
        for right,num in enumerate(nums):
            hashmap[num] += 1            
            while len(hashmap) > k:
                # moving left
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
            # if reach here, it's the max subarray length == k
            # that we need to see how far it can last
            left_cp = left
            hashmap_cp = hashmap.copy()
            count = 0
            while len(hashmap_cp) == k:
                if hashmap_cp[nums[left_cp]] == 1:
                    # 不能再走了，删掉就不是了
                    break
                hashmap_cp[nums[left_cp]] -= 1
                left_cp += 1
                count += 1

            if len(hashmap) == k:
                res += count + 1
        return res
```

## Approach 2: sliding window

有点像recursion和DP中的思路，in approach 1, 我们有个模拟我们`x == k` to `x < k`的过程，并计算count. 但我们可以直接忽略掉这个过程变成，

- max length of the subarray that ends at index 0 that it's # of uniques == k
- max length of the subarray that ends at index 1 that it's # of uniques == k
...
- max length of the subarray that ends at index n-1 that it's # of uniques == k

然后计算

- max length of the subarray that ends at index 0 that it's # of uniques == k-1
- max length of the subarray that ends at index 1 that it's # of uniques == k-1
...
- max length of the subarray that ends at index n-1 that it's # of uniques == k-1

这就变成了经典medium sliding window问题, 我们相减即可.


```python
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums,k):
            n = len(nums)
            res = 0
            left = 0
            hashmap = defaultdict(int)
            for right,num in enumerate(nums):
                hashmap[num] += 1
                while len(hashmap) > k:
                    # moving left
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1
                # if reach here, it's the max subarray length == k
                # that we need to see how far it can last
                res += right - left + 1
            return res
        
        return helper(nums,k) - helper(nums,k-1)
```


## Approach 3 Sliding Window with three pointers

Approach 1的simulation:

- initialize a burner left pointer and burner hashmap to simulate the process of moving left pointer

What if we go that this route early and keep track of another pointer sitting in the middle of left and right pointer? 这就是three pointers思想.

- `l_far`: the farthest left pointer such that `[l_far,right]` is the maximum subarray has k distinct elements in it
- `l_near`: the left pointer such that `[l_near,right]` is the minimum subarray has k distinct elements in it

而且你只维护的hashmap, 实际上是维护的是`[l_near,right]`中的信息. 两者唯一的区别是，维护`[l_far,right]`比维护`[l_near,right]`多了几个redundant元素. 


Do a little dry run,

```
nums = [1,2,1,2,3], k = 2
output = 7
```

|l_far|l_near|r|[l_far,r]|[l_near,r]|candidates|
|---|---|---|---|---|---|
|0|0|0|[1]|[1]||
|0|0|1|[1,2]|[1,2]|`[1,2]`|
|0|1|2|[1,2,1]|[2,1]|`[2,1]`,`[1,2,1]`|
|0|2|3|[1,2,1,2]|[1,2]|`[1,2]`,`[2,1,2]`,`[1,2,1,2]`|
|3|3|4|[2,3]|[2,3]|`[2,3]`|



```python
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        [l_far,l_near]: largest subarray that has k distinct elements in it
        [l_near,r]: smallest subarray that has k distinct elements in it        
        """
        l_far = l_near = 0
        res = 0
        count = defaultdict(int)

        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near
            
            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1


            if len(count) == k:
                res += l_near - l_far + 1

        return res
```