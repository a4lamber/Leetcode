class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Note: LIS
        # base cases: 
        # DP[i] definition: 以index i为起点的LIS的长度
        # transition function: 

        # = 1 case
        if len(nums) == 1: return 1

        # initialize
        LIS = [1 for _ in range(len(nums))]

        # 从倒数第二个index, 做backward iteration
        for i in range(len(nums) - 2, -1, -1):
            # 在i下一个index开始iteration
            for j in range(i+1, len(nums)):
                # 更新DP function
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1) 
            
        return max(LIS)




        
