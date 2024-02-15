---
tags:
    - Array
    - Greedy
    - Sorting
    - Prefix Sum
---

# [2971 Find Polygon With The Largest Perimeter](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15)


## Approach 1 Sorting + Prefix Sum

这题看polygon的形成条件, The longest side of a polygon is smaller than the sum of the other sides, 然后求最大周长的多边形. 转化这个条件为数学公式，我们则有, for a poly with k sides, we have

$$
\begin{equation}
\sum_{i}^{k-1} a_i = a_1 + a_2 + ... + a_{k-1} > a_k
\end{equation}
$$

当你想到最大边要满足大于其它边之和的时候，我的思路直接就转移到是否是DP问题了, 虽然思路错了，但问题转化是对的。要求一个数组`nums`中能组成的polygon with largest parameters, 这个问题的解必然会在以下的子问题之中:

- `dp[i]` : store the largest possible parameters ending with element `i` (`nums[i]`) in the array. 
- `dp[0:2]` == -1, since we need at least 3 elements to form a polygon.

然后我们注意到，在iterate dp, 求每一个`dp[i]`时，都需要知道`nums[0:i]`的解，且每次增幅为one element `nums[i]`, 那我们干脆提前把这个数字的prefix sum计算出来储存在数组里不就好了?

!!! note note
    $O(nlogn) + O(n) \approx O(nlogn)$ in time, $O(n)$ in space

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Condition: if sum(a_1...a_{n-1}) > a_n, then it exists.
        # BFS: O(n!) in time, O(1) in space
        # 1. sort them
        # 2. DP[i]: largest possible parameters ending with element i in the array
        # 3. initial condition: 0s for all. DP[0:2] == 0
        # 4. state transition function:
        # 5. we just need to check if nums[i] < sum(prefixes) if yes, output, if no
        #    we assign as -1
        
        n = len(nums)
        nums.sort()

        # initialize the pre-fix sum
        prefix_sum = [0 for _ in range(n)]
        prefix = 0
        for i in range(n):
            prefix += nums[i]
            prefix_sum[i] = prefix
        
        best = -1
        candidate = -2
        for i in range(2,n):
            if nums[i] < prefix_sum[i-1]:
                candidate = prefix_sum[i]
            
            best = max(best,candidate)

        return best
```

## Approach 2 Prefix Sum Space Optimized

做题的时候没想到，这个`prefix_sum` array可以不用算，可以节约:

- $O(n)$ in space, 因为不需要这个`prefix_sum` array了
- two pass solution to one pass solution

!!! note note
    $O(nlogn) + O(n) \approx O(nlogn)$ in time, $O(1)$ in space


```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        best = -1
        prefix_sum = 0
        for i in range(n):
            if n >= 2:
                if nums[i] < prefix_sum:
                    candidate = prefix_sum + nums[i]
                    best = max(best,prefix_sum + nums[i])

            prefix_sum += nums[i]
        
        return best
```
