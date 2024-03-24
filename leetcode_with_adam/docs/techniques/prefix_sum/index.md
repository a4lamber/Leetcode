# Prefix Sum (前缀和)

前缀和算是一种算法题中的技巧，擅长用于解决整数数组，且出现`subarray sum`或者`contiguous subarray`时可以尝试使用。前缀和的思想是将数组的前缀和存储在一个auxillary data structure中，然后通过计算两个前缀和的差值来得到一个任意subarray的和。
通常auxillary data structure可能是

- 一个hashmap，用于存储前缀和的值as key, 出现的次数，或者index作为value.
- 一个array


Prefix Sum作为技巧，可以和其它算法和数据结构融合。具体的几个高频大类,

- `2 sum系列`
    - 2 sum, 3 sum, 4 sum 
    - 其实contiguous subarray sum也是一种2 sum
- `range sum`
- `sliding window`
    - 只能解决全正数的array, 比如best time to buy and sell stock. 因为sliding window的前提是left pointer move right, subarray sum减少，right pointer move right, subarray sum增加. 但有负数的情况无法保证这一点.
- `monotonic queue`
    - 作为其follow-up



## 相关题目


### Two Sum系列

2 sum, 3 sum, ..., n sum. 这个概念实际是prefix sum的一个特例。prefix sum求的是subarray sum, 也是利用了2 sum中的是`两数之差符合target`.

比较经典的题目有

- 1 two sum
- 560 subarray sum equals k (完全利用了two sum的思想)
- 974 subarray sums divisible by k (转化为560的条件)
- 523 continuous subarray sum (和974完全一样, 用了个小trick)
- 525 contiguous array (binary array of `[0,1]` 转化为 `[-1,1]` 的array, 用了个小trick. 其实也像majority elements里的投票算法，如果遇到majority element + 1, else -1. 用一个counter来记录)

!!! tip
    subarray的题目，第一反应是prefix sum. But if it's subsequence, 首先需要想到到DP. longest increasing subsequence(LIS)比如.

### Range Sum系列

Range Sum利用了前缀和的一些性质, lazy propagation的思维在range update很有用.

- 370 range addition (利用了[lazy propagation](https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/))
- 304 range sum query 2D - immutable (2D的前缀和, pre-processing技巧很像dp in 2D)


### Sliding Window系列

这一部分就讲了一题.

- 209 minimum size subarray sum

### Monotonic Queue系列

这一部分也是, 算是209的follow up了. 有难度的，得想明白为什么要用单调递增队列和凭什么可以左出.

- 862 Shortest Subarray with Sum at Least K

### Others

|number|类型|description|solution|
|---|---|---|-|
|[560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)||subarray sum equals k. 万物之源|[solution](../../leetcode/560-subarray-sum-equals-k/index.md)|
|[325 Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/)||subarray sum equals k, 但是要求最大的subarray|[solution](../../leetcode/325-maximum-size-subarray-sum-equals-k/index.md)|
|[974 Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)|-|转换divisible by k的条件为subarray sum equals k|[solution](../../leetcode/974-subarray-sums-divisible-by-K/index.md)|
|[525 Contiguous Array](https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16)||trick, binary array of [0,1]转化为[-1,1]|[solution](../../leetcode/525-contiguous-array/index.md)|
|[523 Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)||similar to 974 but with a length constrains|[solution](../../leetcode/523-continuous-subarray-sum/index.md)|
|[370 Range Addition](https://leetcode.com/problems/range-addition/description/)|||[solution](../../leetcode/370-range-addition/index.md)|
|[304 Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/description/)|||[solution](../../leetcode/304-range-sum-query-2D-immutable/index.md)|
|[209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)|sliding window||[solution](../../leetcode/209-minimum-size-subarray-sum/index.md)|


