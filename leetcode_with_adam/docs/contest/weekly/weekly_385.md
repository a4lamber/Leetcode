# Weekly 385

1/4, 就做出第一题. 

![](./../assets/q2-4_hard.png)

## [1 Count Prefix and Suffix Pairs](https://leetcode.com/contest/weekly-contest-385/problems/count-prefix-and-suffix-pairs-i/)

给定一个数组比如, `words = ["pa","papa","ma","mama"]`, 求解其中有多少个pairs, 满足 i < j, and words[i] is a prefix and a suffix of words[j]. 例如, 
```
Input: words = ["pa","papa","ma","mama"]
Output: 2
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.  
```

思路如下，

- 写一个helper function, 判断两个word_1是否是word_2的前缀和后缀，like `is_prefix_suffix(word_1,word_2)`
- 枚举所有的i,j pair, 同时满足helper function以及`i < j`

!!! note "复杂度分析"
    时间复杂度是$O(n^2m)$, 空间复杂度是$O(1)$, 其中$n$是words array的长度，$m$是word的长度

```python
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def helper(word_1,word_2):
            if len(word_1) > len(word_2):
                return False
            
            left,right = 0,-1            
            for _ in range(len(word_1)):
                if word_1[left] != word_2[left]:
                    return False                
                if word_1[right] != word_2[right]:
                    return False
            
                right -= 1
                left += 1
            # if reach here
            return True
        
        # do something instead
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if helper(words[i],words[j]):
                    res += 1    
        
        return res
```

## [2 Find the Length of the Longest Common Prefix](https://leetcode.com/contest/weekly-contest-385/problems/find-the-length-of-the-longest-common-prefix/)

先看例子, 
```python
Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
```

给两个数组，每个数组分别取一个成为一个pair, 然后求解所有pairs中，longest common prefix的长度. 我的思路是(TLE了),

- 一个helper function 求length of the common prefix of two numbers, `common_prefix_length(num1,num2)`
- 然后枚举所有的pair, 求解最长的prefix

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def helper(int_1,int_2):
            word_1,word_2 = str(int_1),str(int_2)
            res = 0
            
            for i in range(min(len(word_1),len(word_2))):
                if word_1[i] != word_2[i]:
                    return res
                res += 1
                            
            return res
            
        best = 0
        
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                candidate = helper(arr1[i],arr2[j])
                best = max(best,candidate)
        return best
```

但这个方法TLE, 答案如下.

??? tip "[3043 Find the Length of the Longest Common Prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/)" 
    用两个hashset分别储存arr1和arr2的所有可能的prefix, 然后取交集，最后求解最长的prefix. Solution [here](../../leetcode/3043-find-the-length-of-the-longest-common-prefix/index.md).


## [3 Most Frequent Prime](https://leetcode.com/contest/weekly-contest-385/problems/most-frequent-prime/)


## [4 Count Prefix and Suffix Pairs II](https://leetcode.com/contest/weekly-contest-385/problems/count-prefix-and-suffix-pairs-ii/)


