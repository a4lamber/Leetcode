# 3105 Longest Strictly Increasing or Strictly Decreasing Subarray

## Approach 1
need to maintain two int for recording current longest strictly increasing array and longest strictly decreasing array.


```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best_asc = 1
        best_desc = 1
        res = 1
        
        prev = nums[0]        
        for curr in nums[1:]:
            if curr == prev:
                # reset
                best_asc = 1
                best_desc = 1
            elif curr > prev:
                # increasing, we start to increase
                best_asc += 1
                best_desc = 1
            else:
                best_desc += 1
                best_asc = 1
            
            res = max(res,max(best_asc,best_desc))
            prev = curr
                                    
        return res        
```