# 46 Permutations

## Problem statement

## Introduction
backtracking入门题目，给定一个数组，返回所有的permutation.



## Code implementation
```python
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
```