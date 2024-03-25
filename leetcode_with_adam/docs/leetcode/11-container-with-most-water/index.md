---
tags:
    - Array
    - Two Pointers
    - Greedy
---

# 11 Container with Most Water

贪心 + two pointers的题目

## Approach 1: Two Pointers + Greedy

我们的目标函数是获得container能装最多的水，也就是maximize volume. 我们可以用两个指针，一个指向左边，一个指向右边，然后我们计算当前的volume，然后选择一个方向移动。选择移动的这个决定，就是这一题的考点，贪心的策略, 体积计算公式如下， 

$$
\text{volume} = \text{width} \times \text{height}
$$

随着我们指针不断向中间内缩，我们的宽度都在变小，为了使我们的体积有变大的可能，我们必须"修补"我们较短的那一侧，所以说我们的贪心策略是移动较短的那一侧指针，这样我们才有可能找到更大的体积.


### Code Implementation

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # volume = width * min(height_l,height_r), then we move the min pointer
        # since width decreases, we have to "fix" our shortest stack
        l, r = 0,len(height)-1
        best = 0

        while l < r:
            curr_volume = min(height[l],height[r]) * (r-l)                
            best = max(best,curr_volume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                

        return best
        
```