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
    