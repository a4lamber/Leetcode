def condition(num,x):
    #
    res = ""

    if (num+1) * (num+1) <x:
        res = "move right"
    elif num * num > x:
        res = "move left"
    elif num * num <= x and (num+1) * (num+1) >= x:
        res = "we are here"
    else:
        pass

    return res 

class Solution:
    def mySqrt(self, x: int) -> int:
        # 输入x, 输出y, x is int, y是x的平方根向下取整
        # 转换思路就是找到一个0到x之间的数字，满足平方根的关系
        # 比如x = 8, 2**2 = 2 x 2 =4, 3**2 = 3x3 = 9, 4<8<9, 只需要满足这个关系就可以了
        # 具体算法用binary search

        left = 0
        right = x

        # edge cases:
        if right == 1:
            return right

        # general cases
        while left < right:
            # get the mid 
            mid = left + (right - left)//2

            # check result
            if condition(mid,x) == "we are here":
                if (mid + 1) * (mid + 1) == x:
                    return mid + 1
                else:
                    return mid
            if condition(mid,x) == "move left":
                right = mid + 1
            elif condition(mid,x) == "move right":
                left = mid - 1
        
        
        return left

            