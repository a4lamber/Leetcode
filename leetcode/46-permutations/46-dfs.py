class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            """
            curr: current permutation we building
            """
            # recursion base condition
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                # 在curr里的数字，已经走过了，lock死，略过
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
            ans = []
            backtrack([])
            return ans

