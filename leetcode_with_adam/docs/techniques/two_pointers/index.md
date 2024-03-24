# Two Pointers

> 双指针是一种灵活的思想和技巧，可以单独使用也可以和其他算法一起结合使用。双指针同时使用两个指针，在不同数据结构上(数组，链表，树，图)中辗转腾挪，同向移动，反向移动，快慢速等等来maintain我们的状态和信息.

常见的分成两类:

- 同向指针(两个指针步长不同), line sweep, sliding window, Floyd's Cycle Detection (快慢指针), 单调队列，单调栈
    - 快慢指针: 
        - 找中点，
        - 判断是否有环 Floyd's Cycle Detection
    - sliding window:
        - 双指针同时scan, 一个指针用于扩展窗口，一个指针用于收缩窗口. 扩展收缩的条件取决于题目的需求，常见维护的信息有:
            - 一个窗口内的信息, like rolling sum
            - 指针上的信息，如记录最大值，最小值
        - 用于解决subsequence(subarray或者substring问题). 对于subarray, 只能用于解决positive array, 因为得保证move left pointer会减少，move right pointer会增加.
    - on sorted array: 
        - 如果给定的条件是两个sorted array, 你可以用双指针在两个数组上同时移动，比如merge two sorted array, find common elements in two sorted array等等.
- 反向指针(两个指针从两端向中间移动), 比如binary search.
    - binary search: 用于在有序数组中查找元素，时间复杂度为O(logn). 两指针在两端，往中间移动。



## 相关问题

|number|类型|description|solution|
|---|---|---|---|
|[680 valid palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)|反向指针|-|solution|
|[408 valid word abbreviation](https://leetcode.com/problems/valid-word-abbreviation/description/)|同向双指针on two array|注意判定leading zero and how to handle digits|[solution](../../leetcode/408)|
|[253 meeting rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/)|双指针|-|[solution](../../leetcode/253-meeting-rooms-II/index.md)|
|[1570 Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/)|同向双指针, on two sorted array|利用list of tuple `(index,value)`储存non-zero elements, 然后双指针on two sorted array,进行dot product计算。好题!|[solution](../../leetcode/1570-dot-product-of-two-sparse-vectors/index.md)|
|42 Trapping Rain Water|双指针|-|solution|
|141 linked list cycle|双指针, 快慢指针|-|solution|
|142 linked list cycle II|双指针, 快慢指针|-|solution|
|[340 Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)|同向指针, sliding window|根据条件move left pointer, 维护一个freq map. 注意当freq = 0时需要移除key|[solution](../../leetcode/340-longest-substring-with-at-most-k-distinct-characters/index.md)|
|15 3sum|双指针, sliding window|-|solution|
|[704 Binary Search](https://leetcode.com/problems/binary-search/description/)|双指针, binary search|-|[solution](../../leetcode/704-binary-search/index.md)|
|887 Super Egg Drop|双指针, |-|solution|


## Reference

- 古城算法基础十一, [双指针(上)](https://www.youtube.com/watch?v=81WCEn2kZQE&t=1867s&ab_channel=%E5%8F%A4%E5%9F%8E%E7%AE%97%E6%B3%95) and [双指针(下)](https://www.youtube.com/watch?v=LUI_01Sf1YE&ab_channel=%E5%8F%A4%E5%9F%8E%E7%AE%97%E6%B3%95)

