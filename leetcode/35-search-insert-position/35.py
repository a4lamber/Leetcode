class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(logn) dead giveaway for binary search
        left = 0
        right = len(nums) - 1

        # check for edge case target > nums[-1]
        if target > nums[-1]:
            return len(nums)

        while left< right:
            # mid pointer 
            mid = left + (right - left)//2

            if nums[mid] < target:
                # search space it to the right
                left = mid +1
            elif nums[mid] > target:
                right= mid 
            else:
                return mid
            
        return left 

