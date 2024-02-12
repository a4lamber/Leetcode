---
tags:
    - Array
    - Hash Table
    - Divide and Conquer
    - Sorting
    - Counting
---
# [169 Majority Element](https://leetcode.com/problems/majority-element/description/)

重点是approach 2 Boyer-Moore Voting Algorithm，学习它throw away prefix的思想

## Approach 1 Hash Solution

!!! note Note
    - Time complexity: $O(n)$
    - Space complexity: $O(n)$


```python
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > math.floor(len(nums)/2):
                return num
```

## Approach 2 Boyer-Moore Voting Algorithm

Boyer and Moore这俩人发过很多算法文章，这篇文章专门计算数组种的majority element
是哪个. 

!!! warning warning
    majority element是指出现次数超过一半的元素. 这个算法的assumption是一定有majority element存在于这个array.

因为prefix不影响suffix对于majority element的结论. 如果定义prefix和suffix的划分点为，counter第二次为0. 那么只要你的candidate在suffix中出现的次数超过一半，那么它就是suffix的majority element.

那我们现在有了条件1, 我们又有assumption作为条件2, 那么

- `条件1`:某个数在suffix中出现的次数超过一半，那么它就是suffix的majority element.
- `条件2`: 这个数组必然存在majority element出现在这个数组中.

`条件2`这个数组必然存在majority element $i$ <--等价于--> Majority element $i$ 必然也是以`counter = 0`为separator的suffix和prefix的majority element.

那么根据`条件1`, 我们知道 $i$ 是suffix的majority element, 再根据`条件2`的等价条件, 我们急需一个candidate同时是suffix和prefix的majority element. 那么既然$i$是suffix的majority element, 它也必然是prefix的majority element.

!!! note Note
    - Time complexity: $O(n)$
    - Space complexity: $O(1)$

### Code Implementation

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = None
        for num in nums:
            if counter == 0:
                candidate = num
            
            counter += 1 if num == candidate else -1
        return candidate
```

## Reference

- [Moore-Boyer Voting Algorithm original paper](https://link.springer.com/chapter/10.1007/978-94-011-3488-0_5)