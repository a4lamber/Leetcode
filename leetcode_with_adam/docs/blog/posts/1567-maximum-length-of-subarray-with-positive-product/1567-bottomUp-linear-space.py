class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # 注意并不需求是length of maximum positive product, 只要任何product positive都可以
        # pos: maximum length of positive product ending on nums[i]
        # neg: maximum length of negative product ending on nums[i]

        pos = [0 for _ in range(len(nums))]
        neg = [0 for _ in range(len(nums))]

        # 等于0的情况的初始化和reset, 都被囊括在内了
        if nums[0] < 0: neg[0] = 1
        if nums[0] > 0: pos[0] = 1

        for i in range(1,len(nums)):
            if nums[i] == 0:
                continue
                # do nothing ,since DP at this steps are already zero. 

            if nums[i] > 0:
                pos[i] = pos[i-1] + 1
                if neg[i-1] > 0: # 说明存在negative 
                    neg[i] = neg[i-1] + 1 # 正负得正
                else: # 说明neg[i-1] = 0, 那么之前array有偶数个负号，或者全>0, 或者nums[i-1] == 0
                    # reset to zero
                    neg[i] = 0

            if nums[i] < 0:
                neg[i] = pos[i-1] + 1
                if neg[i-1] > 0: # 说明存在negative
                    pos[i] = neg[i-1] + 1
                else: # neg[i-1] == 0, 那么之前array有偶数个负号，或者全>0, 或者nums[i-1] == 0
                    pos[i] = 0
            
        return max(pos)

                    
        
        

    
