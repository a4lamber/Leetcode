def accumulativeSum(n):
    return int(n * (n+1)/2)

class Solution:
    def countLetters(self, s: str) -> int:

        # 定义俩指针
        left = 0
        right = 0
        total = 0
        
        # 这种out of index的判定，多循环一次
        for right in range(len(s) + 1):
            # change of variable or out of index
            # python if 先判定左侧的，一定要把out of index判定放最前面
            if right == len(s) or s[left] != s[right]:
                len_substring = right - left
                # 等家数列求和
                total += accumulativeSum(len_substring)
                left = right
        return total
