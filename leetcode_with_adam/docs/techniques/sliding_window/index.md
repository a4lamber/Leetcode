# Sliding Window

Sliding window也是一种技巧，是two pointer的一类，但由于太常见了，逐渐自成一脉。Sliding window的核心思想是维护一个窗口 with pointer left and right在both ends of the window. 这个窗口可以是固定大小，也可以是可变大小。通常会维护一些关于窗口内的东西的信息, 比如

- 窗口内的信息, like rolling sum, maximum
- 窗口上的信息

Sliding window常用于解决subsequence. subsequence包括subarray或者substring问题.

- 对于subarray, sliding window只能用于解决positive array, 因为得保证move left pointer会减少，move right pointer会增加.
- 对于substring, 


## 相关问题

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