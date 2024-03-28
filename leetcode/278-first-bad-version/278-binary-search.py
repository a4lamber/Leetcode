# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # intuition, binary seaech O(logn)
        left = 1
        right = n

        while left < right:
            # update mid points to middle of the search space
            mid = (right - left)//2
            
            # bad path
            if isBadVersion(mid):
                # 中位数是bad version, search space在左边,update右指针
                right = mid 
            else:
                # 中位数是good version, search space在右边，update左指针
                left = mid + 1


        
        return left