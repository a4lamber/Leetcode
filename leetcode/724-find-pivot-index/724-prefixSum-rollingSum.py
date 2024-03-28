class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix-sum
        # post-fix sum
        # 辗转相加法
        # search space: 2nd element till 2nd last element; left to right scan
        
        # edge case
        if len(nums) == 1: return 0

        # 初始化以及考虑左边界
        prefix = 0
        postfix = sum(nums[1:])
        if postfix == 0: return 0
        
        for i in range(1,len(nums)-1):
            prefix += nums[i-1]
            postfix -= nums[i]
            if prefix == postfix:
                return i 
        
        # 考虑右边界
        prefix += nums[len(nums)-2]
        if prefix == 0: return len(nums) - 1

        # not found
        return -1

