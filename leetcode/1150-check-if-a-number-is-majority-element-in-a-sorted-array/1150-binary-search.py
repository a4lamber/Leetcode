class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 思路2: binary search to find target; 如果找到了,则从mid为起点往两边辐射
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                # 相等则判断是否是majority
                toLeft = mid
                toRight = mid

                while toLeft - 1 != -1 and nums[toLeft-1] == target:
                    toLeft -= 1
                    

                while toRight + 1 != len(nums) and nums[toRight+1] == target:
                    toRight += 1
                    

                return (toRight - toLeft + 1) > len(nums)//2
                

            if nums[mid] > target:
                # search space to the left
                right = mid -1
            elif nums[mid] < target:
                # search space to the right
                left = mid + 1
        
        # target not found
        return False        




