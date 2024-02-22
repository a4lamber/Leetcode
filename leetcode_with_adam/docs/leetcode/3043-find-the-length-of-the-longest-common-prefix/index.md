# 3043 Find the Length of the Longest Common Prefix

注意到这一题的constrains:

- `1 <= arr1.length, arr2.length <= 5 * 10**4`
- `1 <= arr1[i], arr2[i] <= 10**8`

我们的approach如下:

- 用两个hashset分别存储所有可能的prefix for arr1 and arr2.
- 写一个函数，输入一个string, 输出所有可能的prefix. 由于arr1[i],arr2[i] $\in [1,10^8]$ , 所以每个数的prefix最多有9个. 所以这个函数的时间复杂度是$O(9m)\approx O(m)$, 其中$m$是arr长度.
- 这两个set求交集
- 求交集中的最长的prefix

!!! tip Tip
    把这一题想象成数据库中，两个大表join之前的filtering, 这样你就不需要做full table scan on both table, 然后run cartesian join了.


    



## Approach 1 Hashset

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # longest common prefix of (x,y) for x,y in zip(arr1,arr2)
        # if it's a common prefix, then it must be a prefix in both arrays
        # 有点像filtering b4 joining two big tables in SQL
        # to have two hashset to store the all possible prefix in arr1 and arr2, respectively
        # (1,10,100) (1000) and (1 ,2 ,3) (4) then we find the intersection between a and b. finally we compute for the longest
        # arr1[i],arr2[i] \in (1,10**8)
        # each val in arr1 or arr2, will has maximum of 9 possible prefixes

        def get_all_prefix(word):
            """
            give all possible prefix of this word
            """
            prefixes = []
            left,right = 0,len(word)-1
            while left <= right:
                prefixes.append(word[left:right+1])
                right -= 1
            return prefixes

        nums1 = [str(ele) for ele in arr1]
        nums2 = [str(ele) for ele in arr2]

        set1 = set()
        set2 = set()
        
        
        for num in nums1:
            prefixes = get_all_prefix(num)
            for prefix in prefixes:
                set1.add(prefix)
        
        # O(9 * m) = O(m)
        for num in nums2:
            prefixes = get_all_prefix(num)
            for prefix in prefixes:
                set2.add(prefix)
        
        # now we have two hashset, we just find the intersection of it
        candidates = set.intersection(set1,set2)
        
        # edge case
        if len(candidates) == 0: return 0
        
        res = 0
        for candidate in candidates:
            res = max(res, len(candidate))

        return res
```