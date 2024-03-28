class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            # 不在数组第一位的非0整数;
            if i != 0 and nums[i] != 0:
                # another pointer
                curr = i
                prev = i -1

                # traverse the previous index
                while prev >= 0 and nums[prev] == 0:
                    # inline swap
                    nums[prev],nums[curr] = nums[curr],nums[prev]
                    # move indexes to the left    
                    curr -= 1
                    prev -= 1
                