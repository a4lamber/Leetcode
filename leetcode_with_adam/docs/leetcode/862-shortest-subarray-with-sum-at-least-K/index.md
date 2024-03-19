---
tags:
    - Array
    - Prefix Sum
    - Monotonic Queue
    - Sliding Window
---
# 862 Shortest Subarray with Sum at Least K

Prefix Sum + Monotonic Queue. 是[209 Minimum Size Subarray](../209-minimum-size-subarray-sum/index.md)的follow-up. 209题因为全是正数数组，可以用sliding window. 当你的数组中存在负数的时候，你就无法用sliding window了。这个时候就需要用monotonic queue了.


## Approach 1 Monotonic Queue

分成以下几步:

- pre-processing `nums`, 或者prefix sum的数组，别忘了left padding zero
- 维护一个monotonically increasing queue, linear scan `prefix_sum` array, 对每一个新来的prefix_sum, 进行判定
    - `右出`: 保证queue的严格单调递增. 标准的单调队列操作
    - `左出`: 判断queue中的元素和新来的prefix_sum的差值大于等于k，一直循环到所有符合条件的都pop出去.这一步有几点要注意:
        - window size = 右边新来的index - 左边pop出去的index (目前最小的)
        - monotonic queue中维护的是prefix_sum的index, 那么只可能是[1,2,3] 或者[2]. 不存在大的index在前面，小的index在后面的情况.
        - 虽然第一个`左出`的最小的，那么right - left反而是最大的. 我们还有个`while`呢，总会遇到的?
        - 如果我们popleft()了，以后的array用到怎么办? 不可能，我们以后遇到的，右边界都会比curr right要大，所以window size也会大. 算过就扔掉.

!!! warning
    关键在于想明白为什么可以`左出`, 只要有符合条件的right - left, 我们就计算window size了。之后left就可以扔掉了，因为再往后遇到的right都会比现在的right大，所以window size也会大.


```python
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # pre-processing an array, with left padding zero
        n = len(nums)
        prefix_sum = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)
    
        # small,big,very big 
        # monotonically increasing queue, 保持最小的在左边
        # 里面储存的是符合条件的prefix sum的index
        # cuz k > 0, 我们希望右边的prefix越大越好，左边的越小越好
        res = n+1
        queue = deque()

        for i,curr_sum in enumerate(prefix_sum):
            # 只要我队列里有比这个新来的这个数pre_i大的，统统pop走，保持从左到右是从小到大的
            while queue and curr_sum <= prefix_sum[queue[-1]]: # right out
                queue.pop()
            
            # 把符合条件的，都记录一遍
            # 条件是: pre_i - 单调队列的最小值
            while queue and curr_sum - prefix_sum[queue[0]] >= k: # left out
                res = min(res,i - queue.popleft())

            queue.append(i)

        return res if res != n+1 else -1
```