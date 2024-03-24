---
tags:
    - Heap
    - Hash Table
---

# [3092 Most Frequent IDs](https://leetcode.com/problems/most-frequent-ids/description/)

比赛时想出来了max heap, but我居然在分类讨论各种情况，但不用那么复杂. [Lee215](https://leetcode.com/problems/most-frequent-ids/solutions/4916871/python-heap) solution here.

```
Input: nums = [2,3,2,1], freq = [3,2,-3,1]

Output: [3,3,2,2]

Explanation:

After step 0, we have 3 IDs with the value of 2. So ans[0] = 3.
After step 1, we have 3 IDs with the value of 2 and 2 IDs with the value of 3. So ans[1] = 3.
After step 2, we have 2 IDs with the value of 3. So ans[2] = 2.
After step 3, we have 2 IDs with the value of 3 and 1 ID with the value of 1. So ans[3] = 2.
```

!!! warning "反思"
    维护max heap and hash table for ground truth. 难点在于怎么定义这个max heap
	
    - `max_heap[t]`: At iteration `t`, 所有最好的历史记录 including `curr`. 但一旦历史记录中，有哪些数被更新了, 就需要pop出来, **但不是现在**.
	- 我比赛的时候都在分类讨论，怎么把这些需要被更新的数从heap中pop出来, 但我们其实并不需要马上pop出来, 我们只需要在用的时候pop出来。怎么定义用的时候，就是我们弄的时候, 也就是append to res之前.
  
    这个背后的思想很重要，有点像lazy evaluation, 我们只在需要的时候才去heappop()被update后的值. 即使历史数据cluster在heap中，worst case也只会占据O(n)的空间. 无关紧要的.

## Approach 1: Max Heap + Hash Table

Bookkeeping problem, 维护两个数据结构,

- `hash table`: as the source of truth
- `max heap`: to keep track of the most frequent id, as a tuple (-freq,id). 这里储存的是历史所有的最大值，一旦被修改，所有影响top of heap的, 都必须pop出来.

最关键的一点是想明白,

> 当前的最优解一定出现在以下三种情况中:
> 
>   - brand new的值 like (freq, id) as (100000, 5)
>   - 被篡改id的历史最大值中(也就是说要把老的pop掉), 通常伴随着positive freq operations.
>   - 没有被篡改过的历史最大值中, 通常伴随着negative freq operations.

算法如下,

- linear scan the input
    - update the hash table for source of truth
    - push the (-freq,id) tuple into the max heap.
    - 只要`source of truth`和max heap的frequency不同，就全pop出来. 代表的意义是，历史最大值的id被更新过了，所以需要pop出来，没有价值了. 这时候几种情况:
        - push进去的刚好是heap[0], 我们直接拿出来.
        - push进去的不是heap[0], 但我们max heap中之前的更改过的历史最大值全部pop出去，剩下的就是新的最大值.

!!! tip
    heap一定不为空，因为我们先heappush(heap,(-count[i],i)), 所以至少还有刚push的值在里面.

```python
from collections import Counter
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # maintain a max heap
        heap = []
        count = Counter()
        res = []

        for i,f in zip(nums,freq):
            count[i] += f
            # push in the id
            heappush(heap,(-count[i],i))
            # 只要hashmap中的值和max heap中的值不同，全pop出来
            while heap and count[heap[0][1]] != -heap[0][0]:
                heappop(heap)
            res.append(-heap[0][0] if heap else 0)
        
        return res
```

More cleaner

```python
from collections import Counter
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # maintain a max heap
        heap = []
        count = Counter()
        res = []

        for i,f in zip(nums,freq):
            count[i] += f
            # push in the id
            heappush(heap,(-count[i],i))
            # 只要hashmap中的值和max heap中的值不同，全pop出来
            while count[heap[0][1]] != -heap[0][0]:
                heappop(heap)
            res.append(-heap[0][0])
        
        return res
```