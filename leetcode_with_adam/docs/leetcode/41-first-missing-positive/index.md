---
tags:
    - Array
    - Hash Table
---

# [41 First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26)


## Approach 1 in-place algorithm

intuition:

- solution must be withtin [1,n] for `len(nums) == n`, with edge case of [1,2,3]
 where result is `n+1`

algorithm:

- map `[1,n]` solution space to index `[0,n-1]` of the `nums` by convert it from `int` to `tuple` of `(num, seen?)`
- first pass to mark the array
- second pass to find the value at index `i` that is not a tuple. then `i+1` must be solution
- third pass to revert it back to original states



```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        given unsorted integeter array, return smallest postive integer in nums
        Constraints:
        - O(n) in time O(1) in space
        - n \in [1,10^5]

        Obvervastions:
        - negative number,
        - 0 doesn't count as positive interger, Z^{+}
        - it could be to the left, mid and right
            - [2,3,4] --> 1 left
            - [1,4,2] --> 3 mid
            - [3,1,2,] --> 4 right
        
        potential solution:
        - sort it, [-1,1,3,4] find the first value > 0
            - if it's not 1, we found it to the left
            - if it's 1, we continue to scan until "gap"
            - if it reaches the end, it's end + 1
            - O(nlogn) in time, O(1) in space
        - set(nums) and we check from [1,...x], 
        - it could be large cuz nums[i] \in [-2^31 .. 2^31-1]

        intuition:
        - it is suggested it's a in-place, could be a two-pass 
            - 1st pass to mark the array somehow
            - 2nd pass, just to locate it
        - maintain a global min but positive O(1)
        - the nums size is O(n), which mean we don't care value greater than n, it has to be withtin [1,n] since 
        we can also have negaitve values and values > n to "dilute" the solution space
        - we only care about it, if the value is \in [1,n] and we can mark it somehow to [0,n-1]
        - gaussian sum only works if we only have 1 value not from it. If we have two, we c
        we can "*= -1" [0,n-1] for values [1,n],         
        """
        n = len(nums)
        res = n+1
        
        for i,num in enumerate(nums):
            if type(num) is tuple:
                num , _ = num
            # we only care if num \in [1,n]
            if num >= 1 and num<= n:
                if type(nums[num-1]) is tuple:
                    # we have seen it
                    continue
                nums[num-1] = (nums[num-1], True)
        
        for i,num in enumerate(nums):
            if type(num) is not tuple:
                res = i+1
                break
        
        # revert it back in-place
        nums = [num[0] if num is tuple else num for num in nums]

        # if ever reach here, we can do some logic to check it's 
        return res
```