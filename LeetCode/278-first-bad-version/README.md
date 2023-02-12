# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach: Binary search
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # intuition, binary seaech O(logn)
        left = 1
        right = n

        while left < right:
            # update mid points to middle of the search space, need to consider overflow
            # Example: left = 2**31 - 3, right = 2**31 -1
            mid = left + (right - left)//2

            # bad path
            if isBadVersion(mid):
                # 中位数是bad version, search space在左边,update右指针
                right = mid 
            else:
                # 中位数是good version, search space在右边，update左指针
                left = mid + 1


        
        return left
```