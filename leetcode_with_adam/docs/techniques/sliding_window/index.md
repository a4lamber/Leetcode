# Sliding Window

Sliding window也是一种技巧，是two pointer的一类，但由于太常见了，逐渐自成一脉。Sliding window的核心思想是维护一个窗口 with pointer left and right在both ends of the window. 这个窗口可以是固定大小，也可以是可变大小。通常会维护一些关于窗口内的东西的信息, 比如

- 窗口内的信息
    - rolling sum小于k
    - max element出现的次数 < k
- 窗口上的信息

Sliding window常用于解决subsequence. subsequence包括subarray或者substring问题.

- 对于subarray的rolling sum, sliding window只能用于解决positive array, 因为得保证move left pointer会减少，move right pointer会增加.
- 对于substring, 


## 相关问题

古城算法提供的清单，都是1000以内的sliding window经典.

|number|类型|题型|description|solution|
|---|---|---|---|---|
|[3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|`substring`|sliding window|维护一个set, 用于存储窗口内的信息|[solution](../../leetcode/3-longest-substring-without-repeating-characters/index.md)|
|[159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)|`substring`|sliding window|维护一个freq map, 用于monitor现在的counter|[solution](../../leetcode/159-longest-substring-with-at-most-two-distinct-characters/index.md)|
|[340 Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)|`substring`|sliding window|根据条件move left pointer, 维护一个freq map. 注意当freq = 0时需要移除key|[solution](../../leetcode/340-longest-substring-with-at-most-k-distinct-characters/index.md)|
|395 Longest Substring with At Least K Repeating Characters|`substring`|slidng window|有点难的，小东西!!|[solution](../../leetcode/395-longest-substring-with-at-least-k-repeating-characters/index.md)|
|[209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)|`subarray`|sliding window|维护一个sum, 当sum >= target时, move left pointer, 更新min length|[solution](../../leetcode/209-minimum-size-subarray-sum/index.md)|
|76 Minimum Window Substring|`substring`|sliding window|维护一个freq map, 用于存储窗口内的信息|[solution](../../leetcode/76-minimum-window-substring/index.md)|
|992 Subarrays with K Different Integers|`subarray`|sliding window|维护一个freq map, 用于存储窗口内的信息|[solution](../../leetcode/992-subarrays-with-k-different-integers/index.md)|
|1248 Count Number of Nice Subarrays|`subarray`|sliding window|维护一个freq map, 用于存储窗口内的信息|[solution](../../leetcode/1248-count-number-of-nice-subarrays/index.md)| 



## Lee's List

这个list is provided by lee215, 算是比较新的题.

|number|类型|description|description|solution|
|---|---|---|---|---|
|[2958 Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/)|`subarray`|符合条件的最长|维护hashmap for frequency, 遍历所有right pointer, 当条件不满足时, move left pointer|[solution](../../leetcode/2958-length-of-longest-subarray-with-at-most-k-frequency/index.md)|
|2831 Find the longest equal subarray|nope
|[2799 Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/)|`subarray`|符合条件的个数|维护一个hashmap|[solution](../../leetcode/2799-count-complete-subarrays-in-an-array/index.md)
|[2730 Find the Longest Semi-Repetitive Substring](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/)|`substring`|符合条件的最长|维护一个`int`, 记录pairs次数. 一旦pairs == 2, 移动左指针直至pairs == 1|[solution](../../leetcode/2730-find-the-longest-semi-repetitive-substring/index.md)|
|2555 Maximize Win From Two Segments|
|2537 Count the number of good subarrays|
|2401 Longest Nice Subarray|
|2398 Maximum Number of Robots Within Budget|
|2024 Maximize the confusion of an exam|
|1838 Frequency of the most frequent element|
|1493 longest subarray of 1's after deleting one element|
|1425 Constrained subsequence sum|
|1358 Number of Substrings Containing All Three Characters|
|1248 Count Number of Nice Subarrays|
|1234 Replace the Substring for Balanced String|
|1004 Max Consecutive Ones III|
|930 Binary Subarrays With Sum|
|992 Subarrays with K different integers|
|904 Fruit into baskets|
|862 Shortest subarray with sum at least K|
|424 Longest repeating character replacement|
|209 Minimum size subarray sum|


