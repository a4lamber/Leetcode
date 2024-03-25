---
tags:
  - Array
  - Hash Table
---

# [442 Find all Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25)

> follow-up: can you solve it without extra space and in O(n) runtime? 这一题的trick和prefix sum中[525 Contiguous Array](https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16)很像.

Two things came to my mind are:

- brute force , O(n^2), O(1)
- set, O(n), O(n)

Observation:

- for an array of length n, nums are in the range[1,n] some of those number could be missing from the array
- if an integer appears, it must appear either one or twice. Nothing larger

So it is suggesting a in-place algorithm. We can use index to store whether we have seen the number or not. 
```
value 1,2,3,4,5
index 0,1,2,3,4
```
The ultimate trick is that, we only care if we have seen it before or not. And it at most appears twice. So we can use the sign of the number to mark it. 


!!! tip "interview tip from LC editoral"
    This approach modifies the input. It changes the order of nums, but not the values of nums. In-place algorithms overwrite the input to save space, but sometimes this can cause problems.

    Here are a couple of situations where an in-place algorithm might not be suitable.

    - The algorithm needs to run in a multi-threaded environment, without exclusive access to the array. Other threads might need to read the array too, and might not expect it to be modified.
    - Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.

    In an interview, you should always check whether the interviewer minds you overwriting the input. Be ready to explain the pros and cons of doing so if asked!

    当然，你也可以one-pass scan to modify it back to original array.

## Approach 1 in-place algorithm


```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """

        we sort of need a hashset-like thing to mark what we have seen so far.
        Observation:
        - for an array of length n, nums are in the range[1,n] some of those number could be missing from the array
        - if an integer appears, it must appear either one or twice. Nothign larger
        --> we can try a in-place algorithm
        value 1,2,3,4,5
        index 0,1,2,3,4
        """
        n = len(nums)
        res = []
        for i in range(n):
            curr = abs(nums[i])
            if nums[curr-1] > 0:
                # we haven't seen it, markit
                nums[curr-1] *= -1
            else:
                # we have seen it b4!!
                res.append(curr)

        return res
```