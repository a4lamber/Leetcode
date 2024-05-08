class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two-pointer technique:
        # slow pointer: points to the location of "leading zero" 最左边的0
        # fast pointer：traverse forward and looking for non-zero
        # Note: fast pointer正常traverse, slow pointer 正常traverse直到发现zero, 则停止
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                # swap 
                nums[fast],nums[slow] = nums[slow],nums[fast]

            # slow pointer 往前走一步
            if nums[slow] != 0:
                slow += 1

