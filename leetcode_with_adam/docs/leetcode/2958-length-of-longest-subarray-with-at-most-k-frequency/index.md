---
tags:
    - Array
    - Hash Table
    - Sliding Window
---

# 2958 Length of Longest Subarray with at Most K Frequency

classic sliding window problem.

## Approach 1 Sliding Window

```python
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        maximum freq <= k <--> good, 
        intuition:
            - subarray --> sliding window + hash table as the counter
        traverse the right pointer, maintain a counter, a global max, you wish to update it every step
        and update global_max = max(global_max,local_max) if necessary, until global_max > k, 
        you try to remove the left pointer and those char are already in the hashtable key space        
        """
        res = 0        
        hashtable = defaultdict(int)
        left = 0

        for right,num in enumerate(nums):
            hashtable[num] += 1
            
            while hashtable[num] > k and left < right:
                hashtable[nums[left]] -= 1            
                left += 1
                
            # if reach here, we must have a subarray that's good
            res = max(res,right - left + 1)

        return res
```