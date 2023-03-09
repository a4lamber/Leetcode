# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
we could easily find the target inside the array if it exists but the questions are, what's next? 

My originally thought is to binary search the problem and then radiates out from the target but that would lead to $O(n)$ worst case.

We start from defining the [start,end]:
- nums[start] the 1st value in the array `nums` that satisifies the condition and the index nums[start-1] != target

Then, We could solve the problem into subproblems:
- find the target to see if it exists or not
    - find the left most target 
    - find the right most target

# Approach
<!-- Describe your approach to solving the problem. -->
- create a function to find the target, then binary search it's left search space until **it find last index that satisify the condition.** 
- create a function to find the target, then binary search it's right search space until **it find last index that satisify the condition.** 
- job done!

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Summary
这一题主要学到的:
- 清晰的用语言表达出你要的condition, 这样会给你有启发
- 分治的思想，来将母问题改成俩子问题
- 学到了nested binary search. 

# Code
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(logn) runtime + sorted array,  dead giveaway for binary search
        
        if len(nums) == 0: return [-1,-1]
        if target < nums[0] or target > nums[-1]: return [-1,-1]

        def search_left_most_target(arr,target_value):
            left = 0
            right = len(arr) - 1
            left_most_index = -1
            
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] > target:
                    # search space to the left
                    right = mid - 1
                elif nums[mid] < target:
                    # search space to the right
                    left = mid + 1
                else:
                    # target found, search left
                    left_most_index = mid
                    right = mid - 1
            
            return left_most_index

        def search_right_most_target(arr,target_value):
            left = 0
            right = len(arr) - 1
            right_most_index = -1

            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] > target:
                    # search space to the left
                    right = mid - 1
                elif nums[mid] < target:
                    # search space to the right
                    left = mid + 1
                else:
                    # target found, search right
                    right_most_index = mid
                    left = mid + 1
            
            return right_most_index


        start = search_left_most_target(nums,target)
        end = search_right_most_target(nums,target)

        return [start,end] 
    
        
 



            

```