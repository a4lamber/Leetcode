# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

Binary search算法很简单，但是implement起来的问题有很多, 更多细节可以看 [powerful ultimate binary search template.](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems) 非常好的总结


这些也是很困惑我的问题，如下:
- `right = mid` or `right = mid - 1`?
- `left = mid` or `left = mid + 1`
- `while left < mid` or `while left <= mid`?
- `return left` or `return left-1`

以上的这些boundary的划分，真的非常让我confusing, 这个作者总结的万能套用模版非常漂亮 template如下
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    
    left,right = min(search_space), max(search_space)

    while left < right:
        mid = left + (right - left)//2
        if condition(mid):
            right = mid
        else:
            left = mid +1

    return left 
```
之后只需要用这个模版改就可以了, 有以下几点需要注意：
- `mid = left + (right - left)//2`, 主要为了防止data overflow
- `while left < right`, `right = mid`, `left = mid + 1` 以及`mid = left + (right - left)//2` 这个组合有以下几个特点：
  - **收敛时特点:** 当`left`和`right`的差值为1时，`mid`和`left`就一样，这时候有两种可能:
    - 不满足条件(没找到target), 执行`left = mid + 1`, 那这样, `left == right`, 下一次check `while`条件时候，就过不了了；
    - 满足条件(找到target)时,  不直接`return mid`,而是执行right = mid, 为什么，因为这样的话`right == left == mid`三者都相等，`return left` 即可 



# Approach: Binary search
<!-- Describe your approach to solving the problem. -->



# Complexity
- Time complexity: $O(logn)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # intuition, binary seaech O(logn)
        left = 1
        right = n

        while left < right:
            # update mid points to middle of the search space, need to consider overflow
            # Example: left = 2**31 - 3, right = 2**31 -1
            mid = left + (right - left)//2

            # bad path
            if isBadVersion(mid):
                # 中位数是bad version, search space在左边,update右指针
                right = mid 
            else:
                # 中位数是good version, search space在右边，update左指针
                left = mid + 1


        
        return left
```