# Bi-Weekly History

**biweekly 128**

2/4, 第三题graph, 我还没学。第四题感觉是个monotonic queue, 我很close了，但是没写出来。

|number|description|solution|
|---|---|---|
|[3110 Score of a String](https://leetcode.com/problems/score-of-a-string/description/)|adjacency pair的问题|[solution](../../leetcode/3110-score-of-a-string/index.md)|
|[3111 Minimum Rectangles to Cover Points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/)|simulation|[solution](../../leetcode/3111-minimum-rectangles-to-cover-points/index.md)|
|-|-|-|
|[3113 Find the Number of Subarrays Where Boundary Elements Are Maximum](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/)|monotonically decreasing queue|[solution](../../leetcode/3113-Find-the-Number-of-Subarrays-Where-Boundary-Elements-Are-Maximum/index.md)|


**biweekly 127**

2/4, 可惜的是第三题是标准sliding window题目，不过prefix-sum被替换成了`bit OR`的操作以及nullify nums[left]. 为了能 准确的nullify, 需要维护一个32的数组来记录每个bit的出现次数.

|number|description|solution|
|---|---|---|
|[3095 shortest subarray with OR at least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/)|brute force|[solution](../../leetcode/3095-shortest-subarray-with-OR-at-least-K-I/index.md)|
|[3096 Minimum Levels to Gain More Points](https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/)|prefix sum的题目|[solution](../../leetcode/3096-minimum-levels-to-gain-more-points/index.md)|
|[3097 Shortest Subarray with OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/)|sliding window, bit manipulation|[solution](../../leetcode/3097-shortest-subarray-with-OR-at-least-K-II/index.md)|
|3098 Find the Sum of Subsequence Powers|
