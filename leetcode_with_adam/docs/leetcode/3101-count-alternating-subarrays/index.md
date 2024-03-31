# [3101 Count Alternating Subarrays](https://leetcode.com/problems/count-alternating-subarrays/)

Adjacency pairs are alternating if they are different.

## Approach 1 Sliding Window

```python
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        """
        observation:
        - if a subarray of size n, has n-1 pairs. those pairs are alternating like [0,1,0,1]
        - nums is either 0 or 1
        - if a array like [0,1,0,1] then its children [1,0,1] and [0,1] amd [1] is also a subarray
        
        objective:
        - find the maximum alternating subarray ending at index 0
        - find the maximum alternating subarray ending at index 1
        - ...
        - find the maximum alternating subarray ending at index n-1
        dry run of [0,1,1,1]
        - i = 0, [0]
        - i = 1, [0,1]
        - i = 2, [1]
        - i = 3, [1]
        dry run of [1,0,1,0]
        - i = 0, [1]
        - i = 1, [1,0]
        - i = 2, [1,0,1]
        - i = 3, [1,0,1,0]
        """
        if len(nums) == 1:
            return 1
        
        left = 0
        res = 1
        prev = nums[left]
        
        for right,curr in enumerate(nums[1:],1):
            if curr == prev:
                left = right
                res += 1
                continue
            prev = curr
            res += right - left + 1
            
        return res
```