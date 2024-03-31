
# [3096 Minimum Levels to Gain More Points](https://leetcode.com/problems/minimum-levels-to-gain-more-points/)

最优解O(n) in time, O(1) in space. Prefix sum的题目.

## Approach 1 Prefix Sum

Observation:

- nums[i] == 0, 扣1分; nums[i] == 1, 加1分
- daniel starting from level 0, and bob starting from where daniel left the game
- daniel 和 bob至少各玩一次


```python
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        """
        nums[i] == 0 then it's impossible
        
         0 1 2 3
        [1,0,1,0]
        
        we convert it to binary
        [1,-1,1,-1]
        Objective:
        - we tryna find the minimum length of subarray starting at index 0, such that the remaining subarray won't outscore it
        """
        nums = [-1 if num == 0 else num for num in possible]
        res = - 1
        n = len(nums)
                
        daniel = 0
        bob = sum(nums)
        for i,num in enumerate(nums):
            bob -= num
            daniel += num
            if daniel > bob and i != n-1:
                return i + 1
                
        return res
```

进行优化,

- 可以不需要O(n)数组来flip 0 to -1. 我们可以直接在原数组上操作, 多一些判定语句罢了.


```python
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        res = - 1
        n = len(possible)
                
        daniel = 0
        # sum(possible): 多少个1; n: 总共多少个数字;
        bob = sum(possible) - 1 * ( n - sum(possible))

        for i,num in enumerate(possible):
            # daniel加分，bob减分
            daniel += 1 if num else -1
            bob += -1 if num else 1
            if daniel > bob and i != n-1:
                return i + 1
                
        return res
```