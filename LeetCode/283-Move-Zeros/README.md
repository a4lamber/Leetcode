# Approach 1: two pointer technique
<!-- Describe your approach to solving the problem. -->

# Problem
首先转换题干中的条件,
- move all 0's to the end of array
- all the non-zero elements must retain their original order.

这一步转换很重要，可以方便你判断问题. 首先, 这俩条件是mutually exculusive的，也就可以分开完成；

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
这一题two pointer technique，由于我们想要move 0 to the right hand side of array, 同时non-zero element retain order at left hand side of the array, 有一个操作能同时达成以上这两件事:
> 操作: pointer向右scan的过程中,将你遇到的一个non-zero element,停下来，向左scan,与每一个0进行换位，直到遇到另一个non-zero element. 这时pointer继续向前走;

我原先也是这个思路, 找到非0 element,但我是iterative的让1和每一个0,做一次交换位置，我当时的$O(n^2)$的解法[click here](./283-brute-force.py). 为什么这个操作不efficient的原因，就在于我在swap non-zero with zero elements的时候，不止交换了一次位置;

最优解是，我可以只交换一次位置, 也就是如下操作

> 操作: pointer向右scan的过程中,**将你遇到的一个non-zero element**,停下，然后与一个在**最左侧的0** (如果与第二个0交换，则还有0在这个non-zero element左侧)进行位置交换.

要完成以上这个操作，你需要两个信息，遇到的第一个non-zero element, 最左侧的0, 这也就是two pointer comes in的地方:
- `slow pointer`: stays at the leading 0 and waiting to be swapped.
- `fast pointer`: looking for the first non-zero element.

往前走的逻辑:
- `slow pointer`: moves forward by one, if current value is not zero. Stays at that location and waits for being swapped.
- `fast pointer`: just traverse forward by one.

所以可以根据此，可以写出以下代码

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two-pointer technique:
        # slow pointer: points to the location of "leading zero" 最左边的0
        # fast pointer：traverse forward and looking for non-zero
        # Note: fast pointer正常traverse, slow pointer 正常traverse直到发现zero, 则停止
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                # swap 
                nums[fast],nums[slow] = nums[slow],nums[fast]

            # slow pointer 往前走一步
            if nums[slow] != 0:
                slow += 1


```