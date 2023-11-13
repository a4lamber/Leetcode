# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Since list is sorted, binary search comes to my mind. This is a variation of binary search problem.
# Approach
<!-- Describe your approach to solving the problem. -->
- use binary search to find target
    - if not found, `return False` 
    - if found
        - create two pointers `midToLeft` and `midToRight`
        - moves these pointers to the left and tight until reaches the end of the array or `nums[midToLeft] != target`.
        - calculate the total length and compare with half of the array

# Complexity
- Time complexity: `O(logn)`
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # intuition: binary search to find target; if found, radiates out from mid to find its length
        
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = left + (right - left)//2

            # target found!
            if nums[mid] == target:

                midToLeft = mid
                midToRight = mid

                # move pointer to left and right till boundary or target not found
                while midToLeft - 1 != -1 and nums[midToLeft-1] == target:
                    midToLeft -= 1                    

                while midToRight + 1 != len(nums) and nums[midToRight+1] == target:
                    midToRight += 1
                    
                
                return (midToRight - midToLeft + 1) > len(nums)//2
                

            if nums[mid] > target:
                # search space to the left
                right = mid -1
            elif nums[mid] < target:
                # search space to the right
                left = mid + 1
        
        # target not found
        return False        



```