# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

教科书式的binary search problem, 首先需要注意的是, binary search的一个条件:
> 当search space为0时的判定依据为, left bound is to the right of the right bound, 且left - right = 1;

运用这个性质，这一题就简单了


# Approach
<!-- Describe your approach to solving the problem. -->

略



# Complexity
- Time complexity: $O(logn)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left and right bound of the search space
        left = 0
        right = len(nums) - 1

        # iterative solution of binary search
        while left <= right:
            # get mid index by floor division
            mid = (right + left) //2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # when search space is gone, left - right = 1
        return left
```