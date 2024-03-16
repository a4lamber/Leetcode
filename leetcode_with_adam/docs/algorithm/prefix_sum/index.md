# Prefix Sum (前缀和)

前缀和用于解决subarray sum求和为target的subarray的问题。前缀和的思想是将数组的前缀和存储在一个auxillary data structure中，然后通过计算两个前缀和的差值来得到一个任意subarray的和。通常auxillary data structure是一个hashmap，用于存储前缀和的值as key, 出现的次数，或者index作为value。前缀和的时间复杂度是O(n)，空间复杂度是O(n)。


## 相关题目

|number|考点|description|solution
|---|---|---|-|
|[560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)||subarray sum equals k. 万物之源|[solution](../../leetcode/560-subarray-sum-equals-k/index.md)|
|[974 Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)|-|转换divisible by k的条件为subarray sum equals k|[solution](../../leetcode/974-subarray-sums-divisible-by-K/index.md)|
|[525 Contiguous Array](https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16)||trick, binary array of [0,1]转化为[-1,1]|[solution](../../leetcode/525-contiguous-array/index.md)|
|[523 Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)||similar to 974 but with a length constrains|[solution](../../leetcode/523-continuous-subarray-sum/index.md)|
|[370 Range Addition](https://leetcode.com/problems/range-addition/description/)|||[solution](../../leetcode/370-range-addition/index.md)|
|304 Range Sum Query 2D - Immutable|||
|209 Minimum Size Subarray Sum|||