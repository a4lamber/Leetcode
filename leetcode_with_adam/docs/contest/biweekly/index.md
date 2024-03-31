# Bi-Weekly History

**biweekly 127**

2/4, 可惜的是第三题是标准sliding window题目，不过prefix-sum被替换成了`bit OR`的操作以及nullify nums[left]. 为了能 准确的nullify, 需要维护一个32的数组来记录每个bit的出现次数.

|number|description|solution|
|---|---|---|
|[3095 shortest subarray with OR at least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/)|brute force|[solution](../../leetcode/3095-shortest-subarray-with-OR-at-least-K-I/index.md)|
|[3096 Minimum Levels to Gain More Points](https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/)|prefix sum的题目|[solution](../../leetcode/3096-minimum-levels-to-gain-more-points/index.md)|
|[3097 Shortest Subarray with OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/)|sliding window, bit manipulation|[solution](../../leetcode/3097-shortest-subarray-with-OR-at-least-K-II/index.md)|
|3098 Find the Sum of Subsequence Powers|
