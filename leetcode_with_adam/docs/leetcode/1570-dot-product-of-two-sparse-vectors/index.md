---
tags:
    - Array
    - Hash Table
    - Design
    - Two Pointers
---

# 1570 Dot Product of Two Sparse Vectors

题目给了俩很大的sparse vector, 问怎么求dot product比较efficient. 重点在于**sparse vector**, 该怎么样储存比较efficient的问题，我想到几个方法,

- 存成array, 但是这样会浪费空间
- 存成hash table
- [联想到了skyline storage](https://en.wikipedia.org/wiki/Skyline_matrix#:~:text=Skyline%20storage%20has%20become%20very,and%20systems%20of%20equations%20from) in FEA. 但这个是for sparse matrix with symmetric property. 但思路可以借鉴.

!!! warning "Follow-Up from Meta"
    What if one of the vectors is sparse and another is very dense? It means $L_1$ is very large and $L_2$ is very small. How can you optimize your solution?
    这题还有一个姐妹题，也可能被问 [311 Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/description/)

[StrongHire](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/1823242/clean-solutions-for-meta-interview-with-potential-follow-ups) from New York University的答案很不错. 我们先来总结一下四种方法,

|Method|Time|Space|Note|
|---|---|---|---|
|Array|$O(m+n)$|$O(m+n)$|不管sparse vector,全存下来，又慢又浪费空间|
|Hash Set|$O(min(L_1,L_2))$|$O(L_1+L_2)$|用hash set存储非0值，缩小储存空间。但数据量一大，还是有hash collision|
|Two Pointers|$O(L_1+L_2)$|$O(L_1+L_2)$|我们怎么既要只储存non-zero, 而不用hashset呢? 牺牲一点时间，用Array储存`(index,value)` pair, 然后用双指针遍历.|
|Binary Search|$min(L_1,L_2)\log (max(L_1,L_2))$|$L_1 + L_2$|由于一个vector很大，另一个很小，所以$\approx log(max(L_1,L_2))$|

where $m$ and $n$ are the number of elements in the two vectors, and $L_1$ and $L_2$ are the number of non-zero elements in both vectors.

## Approach 1: Array

没啥好说的, brute force. O(n) in time (constructing the sparse vector and also dot product), O(n) in space (storing the sparse vector).

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for num1,num2 in zip(self.nums,vec.nums):
            res += num1*num2
        return res
```


## Approach 2: Hash Set


对于sparse vector, 有很多0值是无意义的，我们可以用hash set来存储非0值，for a vector with 1 million values with 900 thousand zeros, 这样可以节省90%的空间. 

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.lookup = dict()
        # kay:value pair as index:value
        for index,num in enumerate(nums):
            self.lookup[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key in self.lookup.keys():
            if key in self.lookup.keys():
               res += self.lookup[key] * vec.lookup[key]
        return res
```

当然，上述还有一些优化空间，我们可以遍历较小的hash set, 这样可以减少时间复杂度.

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.lookup = dict()
        # kay:value pair as index:value
        for index,num in enumerate(nums):
            self.lookup[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # choose the minimum
        if len(vec.lookup) < len(self.lookup):
            return vec.dotProduct(self.lookup)
        
        # traverse自己
        res = 0
        for key in self.lookup.keys():
            if key in self.lookup.keys():
               res += self.lookup[key] * vec.lookup[key]
        return res

```

!!! tip
    这个方法不够优秀，虽然hash set规避了zero value储存的空间浪费，但是如果input size太大，你不可避免的会发生hash collision, 一般对于hash collision, 我们有以下几个手段，这时候有以下几个solution:

    - 设计更好更快, 更贴合input的hash function
    - `open addressing`: 如果hash function后，发生了collision, 就找下一个空的slot.
    - `chaining`: 如果hash function后，发生了collision, 就把这个值放在一个linked list里面，如果要寻找一个数，就deny it. 如果这个linked list大到不可忍受, 就转化为[红黑树](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree).


试想一下，instead of 1 million data, we have 1 billion vector with 100 million zeros, 这个hash set就会变得很大，这个时候就会发生hash collision. 有没有比hashset更好的方法呢? 这时候我们该怎么办?

!!! note
    load factor: $\alpha = \frac{n}{m}$, where $n$ is the number of elements and $m$ is the number of slots. 是用来表征on average, how many elements are in each slot. 如果$\alpha$ is too large, 就会更hash collision. 一般设计load factor是0.7, 假设我们有100个数，就需要allocate $100/0.7\approx 143$个slots. Idea is similar to [safety factor](https://en.wikipedia.org/wiki/Factor_of_safety) in engineering design.


## Approach 3: Two Pointers 

同向，双指针在两个array上用, 由于我们是linear scan array来构成我们的list of pairs, 所以已经是sorted的了，我们正好可以利用two pointers来解决这个问题.

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = [(i,num) for i,num in enumerate(nums) if num != 0]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        O(L1 + L2) in time, O(L1+L2) in space, where L1 and L2 are number of non-zeros elements in both vec
        """
        curr_i_1 = curr_i_2 = 0
        res = 0
        while curr_i_1 < len(self.pairs) and curr_i_2 < len(vec.pairs):
            # equal
            if self.pairs[curr_i_1][0] == vec.pairs[curr_i_2][0]:
                res += self.pairs[curr_i_1][1] * vec.pairs[curr_i_2][1]
                curr_i_1 += 1
                curr_i_2 += 1
            elif self.pairs[curr_i_1][0] < vec.pairs[curr_i_2][0]:
                # < , move the LHS
                curr_i_1 += 1
            else:
                # > , move the RHS
                curr_i_2 += 1
        return res
```


## Approach 4: Binary Search (Meta Follow-Up)

面试官问你，当你两个vector, 一大一小，你有什么策略吗? 我们回到最基本的思路，以空间换时间，我们可以用binary search来解决这个问题. 



```python
from bisect import bisect_left
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = [(i,num) for i,num in enumerate(nums) if num != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.pairs) > len(vec.pairs):
            return vec.dotProduct(self)

        res = 0
        # linear scan smaller array, binary search in larger array
        for target_i,target_val in self.pairs:
            candidate_val = self.binary_search(vec.pairs,target_i)
            res += target_val * candidate_val

        return res
    
    def binary_search(self,pairs,target):
        """
        return the value if exists else 0
        """
        left,right = 0,len(pairs)-1
        while left <= right:
            mid = left + (right - left)//2
            if pairs[mid][0] == target:
                # found it
                return pairs[mid][1]
            elif pairs[mid][0] > target:
                # solution space to the left
                right = mid - 1
            else:
                # solution space to the right
                left = mid + 1
    
        # not found
        return 0
        
```


# Reference

- [hashing, hashing algorithms and hash collision](https://www.youtube.com/watch?v=HHQ2QP_upGM&ab_channel=PracticalNetworking)
    - 学到了一个hashing function用数学的解释角度. hashing function的转化input to a finite signature. 但input size是infinite的。把无限的问题用有限的描述出来，在数据量小的时候，这个问题是不明显的，但是当数据量大的时候，这个问题就会显现出来，这就是hash collision.