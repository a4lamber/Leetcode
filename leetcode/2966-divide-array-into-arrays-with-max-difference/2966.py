class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(0, len(nums), 3):
            # since sorted
            if nums[i + 2] - nums[i] > k:
                return []
            temp = [nums[i], nums[i + 1], nums[i + 2]]

            res.append(temp)

        return res
