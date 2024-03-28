class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # the range must be between 1 to num

        left = 1
        right = num

        while left <= right:
            mid = left + (right - left)//2

            if mid * mid == num:
                return True
            
            elif mid * mid < num:
                # search space to the right 
                left = mid + 1
            else:
                # search space to the left
                right = mid - 1
            

        return False
