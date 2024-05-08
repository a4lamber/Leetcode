class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 等加数列求和
        if n == 1: return 1


        def get_total_coins(num_of_stairs):
            return (num_of_stairs * num_of_stairs + num_of_stairs)/2

        left = 1
        right = n

        while left <= right:
            mid = left + (right - left)//2

            if get_total_coins(mid) == n:
                return mid
            if get_total_coins(mid) > n:
                # search space to the left
                right = mid - 1
            if get_total_coins(mid) < n:
                left = mid + 1
        # 没建满
        return left - 1


        

        

