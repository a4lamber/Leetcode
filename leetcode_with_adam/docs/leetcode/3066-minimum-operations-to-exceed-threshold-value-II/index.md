---
tags:
    - Array
    - Heap (Priority Queue)
    - Simulation
---

# [3066 Minimum Operations to Exceed Threshold Value II](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/)

According to the constraints, we can guess that the time complexity of the solution should be O(nlogn) or O(nlogk) or O(klogk), where k is the maximum value in the array, n is the length of the array.

**Constraints:**

- `2 <= nums.length <= 2 * 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

With that in mind, the brute force solution is to do n operations, each time we remove the smallest two elements and add the result back to the array. It will be

- $O(nlogn)$ for initial sorting descending
- linear pass for n operations
    - removing the smallest two elements at `nums[-1]`, `nums[-2]` with coast of 2 * $O(1)$
    - adding the result back to the array with binary search $O(logn)$

It will be $O(nlogn)$ + $O(nlogn)$ $\approx$ $O(nlogn)$

But there are something easier than accessing the smallest two elements at tail of the array. We can use a heap to maintain the smallest two elements in the array.

```python
from heapq import heapify,heappush,heappop
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # min(x,y) * 2 + max(x,y) > max(x,y)
        # we can maintain a sorted array of the after operations vals
        """
        [1,1,2,4,9] --> [2,4,9]
                    --> [3]
        [2,4,9] --> [4,9]
        [3]     --> [7]
        
        [4,9] --> [9]
        [7]   --> [15]
        """        
        heapify(nums)
        res = 0

        # at least 2 elements
        while len(nums) > 1:
            small = heappop(nums)
            second_small = heappop(nums)
            
            if small >= k:
                break
            # update 
            curr = small * 2 + second_small
            heappush(nums,curr)
            res += 1
        
        return res
```