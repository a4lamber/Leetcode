# [164 Maximum Gap](https://leetcode.com/problems/maximum-gap/description/)


## Approach 1: Bucket Sort

bucket sort的两个关键点：
- 每个bucket的长度? 即每个bucket的范围是多少？
- 有多少个bucket？


我们希望每个bucket的长度相同, 

$$
\begin{equation}
\text{bucket\_length} = \max(1,\lfloor{{\max(nums) - \min(nums)} \over {len(nums) - 1}}\rfloor) \tag{1}
\end{equation}
$$


确定bucket的数量

$$
\begin{align}
\text{num\_of\_buckets} &= \lfloor{{\max(nums) - \min(nums)} \over {\text{bucket\_length}}}\rfloor + 1 \\
&= \lceil{{\max(nums) - \min(nums)} \over {\text{bucket\_length}}}\rceil 

\tag{2}
\end{align}
$$


如果确定哪个element属于哪个bucket, 可以用下面的公式

$$
 {{nums[i] - \min(nums)} \over {\text{bucket\_length}}}\tag3
$$


## References

- [Hao Kun Yun on CN LC](https://leetcode.cn/problems/maximum-gap/solutions/498577/python3-tong-pai-xu-by-yanghk/)