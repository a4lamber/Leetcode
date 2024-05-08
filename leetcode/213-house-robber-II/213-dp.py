class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP[i]: maximum amount of money you can rob after visiting i consecutive houses
        # The solution will be either case 1 or case 2:
        # case 1: include first house, exclude last house
        # case 2: exclude first house, include last house
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def helper(nums, start, end):
            prevprev = nums[start]
            prev = max(nums[start], nums[start + 1])
            curr = prev
            for i in range(start + 2, end):
                curr = max(prev, prevprev + nums[i])
                prevprev, prev = prev, curr
            return curr

        case_1 = helper(nums, 0, len(nums) - 1)
        case_2 = helper(nums, 1, len(nums))
        return max(case_1, case_2)
