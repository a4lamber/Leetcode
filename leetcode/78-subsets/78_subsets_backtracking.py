class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decide to include (goint left)
            subset.append(nums[i])
            dfs(i+1)

            # decide not to include
            subset.pop()
            dfs(i+1)

        # initiate
        dfs(0)
        return res