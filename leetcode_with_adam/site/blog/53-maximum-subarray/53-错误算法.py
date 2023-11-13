class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 这是一个错误算法，反例就是
        # [8,-2,-4,-1,-8,3,8,8,3,4,2,-9,-1,-3,-6,8,-3,9]
        # 不一定非要包含最大的点，如果是最大的连续subarray也行
        # 只能过 202/210 test cases
        
        # sliding window approach
        # 利用这个性质, 最大的subarray,必然包含着数组中最大的数;
        # 那么我们可以用sliding window以最大数左右辐射开

        # Step1 : 找到最大值和最大的index
        # determine the max value, O(n) operation
        max_index = []
        max_value = float('-inf')
        for num in nums:
            if max_value < num:
                max_value = num
                
        for i in range(len(nums)):
            if nums[i] == max_value:
                max_index.append(i)
        



        res = []
        # Step 2: 沿着所有可能性的最大值往两边辐射
        for pointer in max_index:
            # define two current sums
            curr_max = nums[pointer]
            largest_max = nums[pointer]        
            largest_right_max = nums[pointer]        
            largest_left_max = nums[pointer]        

            # 
            if pointer == 0:
                # 向右辐射
                for i in range(1,len(nums),1):
                    # 求现在最大值
                    curr_max += nums[i]
                    if curr_max > largest_max:
                        largest_max = curr_max

            elif pointer == len(nums) - 1:
                # 向左辐射
                for i in range(len(nums)-2,-1,-1):
                    curr_max += nums[i]
                    if curr_max > largest_max:
                        largest_max = curr_max
            else:
                # 说明在中间，向左右辐射
                left_curr_max = nums[pointer]
                right_curr_max = nums[pointer]
                
                # 向右辐射
                for i in range(pointer+1,len(nums),1):
                    right_curr_max += nums[i]
                    if right_curr_max > largest_right_max:
                        largest_right_max = right_curr_max
                
                # 向左辐射
                for i in range(pointer-1,-1,-1):
                    left_curr_max += nums[i]
                    if left_curr_max > largest_left_max:
                        largest_left_max = left_curr_max

                # 求和
                largest_max = largest_left_max + largest_right_max - nums[pointer]

            res.append(largest_max)
        
        return max(res)  




  

        
        
            

            
                

            
        

        # for i in range(len(nums)):
        #     # 比较是否是当前遇到的最大值
        #     if nums[i] > curr_max:
        #         curr_max = nums[i]
                

