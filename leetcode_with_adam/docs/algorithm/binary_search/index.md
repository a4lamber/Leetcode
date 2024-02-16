# Binary Search Template

Binary search, 本身的思路并不难，难就难在

- should we use `while left <= right` or `while left < right`?
- should we update left pointers as `left = mid` or `left = mid + 1`?
- do we return `left` or `left - 1`

binary search可以有多种写法，如果每次都写的不一样，就会造成对于结束条件，指针变化的混乱，所以我们要找到一种固定的模板，通过修改模板来解决题目. 

## Templates

有很多大神的经验，总结出来了很多模版。这里我们根据一些经典binary search题目作为metrics, 来评价一下这个模版的general性.


### Template 1: Comment from LC

这个template是[704 binary search](https://leetcode.com/problems/binary-search/editorial/)的editorial下面回复区提供的模版.

```python
def search(self, nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    if nums[lo] == target:
        return lo
    else:
        return -1
```



## Reference

- [一个大神的gitbook, 九章算法提供的模版](https://lefttree.gitbooks.io/leetcode-categories/content/BinarySearch/binarySearch.html)
- [地里总结binary search, 评论区大佬厉害](https://www.1point3acres.com/bbs/thread-432793-1-1.html)
- [LC的高赞post](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
- [Topcoder blog, 按照离散，实数集进行分类很理解，难度高，但系统](https://www.topcoder.com/thrive/articles/Binary%20Search)


