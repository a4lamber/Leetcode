---
tags:
    - Array
    - Binary Search
---
# 1011 Capacity To Ship Packages Within D Days


## Approach 1 Binary Search

Binary search 经典题目, 对理解左右边界更新条件很有帮助.

- `left,right的选择` 至少需要`max(weights)`, 不然过不了一天；最多需要`sum(weights)`, 一天就搬完全部了.
- `helper function(weights,guess)`: 用来计算在这个搬运速度`guess`下，需要多少天搬完, 比较tricky, 需要分类讨论
    - 如果搬完今天还有剩余, 那么我们尝试明天继续搬, `i++`
    - 如果搬完今天正好, 那么我们尝试明天继续搬, 所需消耗总天数+1, 然后我们能量值reset. i.e. `i++`, `days_needed += 1`, `remaining = daily_capacity`
    - 如果搬完发现能量不足以搬完，那么我们上一步就已经耗完所有能量了, 所需消耗总天数+1, 然后我们能量值reset以崭新的精神面貌重新面对新一天的工作. i.e. `i++`, `days_needed += 1`, `remaining = daily_capacity`

这个helper function有一个edge case，就是在第一种情况时，我们已经到了最后一个货物 因为不管你再有多少能量，已经没货物给你搬运了, 所以`days_needed += 1`, 收工!

关于左右边界的更新, `if days_needed(weights,mid) <= days:` 说明我们搬运速度过快了，我们需要更慢一点，但我们的solution space肯定在这半块，因为也存在`days_needed(weights,mid) == days`, 所以我们采取比较保守的更新策略，以防truncate掉最优的solution `right = mid`.

`if days_needed(weights,mid) > days`: 说明我们搬运速度过慢了，我们需要更快一点. 因为`days_needed(weights,mid) > days`, 我们的solution space必然不在这半块，所以我们可以更aggressive的更新. `left = mid + 1`

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # find least weight capacity of the ship
        left,right = max(weights), sum(weights)

        def days_needed(weights,daily_capacity):
            days_needed = 0
            remaining = daily_capacity
            
            i = 0
            while i < len(weights):
                remaining -= weights[i]
                if remaining > 0:
                    i += 1
                    # for edge case, 虽然还有capacity,但是到头了+1天
                    if i == len(weights):
                        return days_needed + 1
                elif remaining == 0:
                    # we just found enough, reset our capacity and move on
                    days_needed += 1
                    remaining = daily_capacity
                    i += 1                    
                else:
                    # we can't do today, 重头再来一次
                    days_needed += 1
                    remaining = daily_capacity
                            
            return days_needed

        while left < right:
            mid = (left + right)//2
            if days_needed(weights,mid) <= days:
                # 太快了, 答案在这个solution space里，propogate strategy mild一点
                right = mid
            else:
                # 太慢了
                left = mid + 1

        return left
```

