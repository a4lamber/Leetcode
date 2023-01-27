# Readme
> Tip: LeetCode算法submit时，会给一个比较大的算例，来算runtime和memory consumption，主要是用来区分好的算法和差的算法

这一题我下意识的解法是, traverse这个list twice with nested loop, 然后根据题目做两个if判断:
- 两个element之和等于本身
- 不能用同样的element twice
之后只需要break out the nested loop就可以了, 代码如下
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define return list
        result = []
        # define flag variable to breakout nested loop
        break_out_flag = False
        for i, item_x in enumerate(nums):
            for j, item_y in enumerate(nums):
                # check for two conditions
                # 1. sum of two variables equals to target
                # 2. make sure it's not same elements
                if item_x + item_y == target and i != j:
                    result.append(i)
                    result.append(j)

                    # added a flag variable to break out nested loop
                    break_out_flag = True
                    break
            if break_out_flag:
                break

        return result
```
这一题的时间复杂度是$O(n^2)$, 因为`nums`的size是n， 然后nested loop比较了所有的情况，也就是$n \times n$.



