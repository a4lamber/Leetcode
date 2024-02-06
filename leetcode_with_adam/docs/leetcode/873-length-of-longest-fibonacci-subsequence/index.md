---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Approach 1: Bottom-up, linear space, `DP[i][j]` ending on 

For this question, it is asked to find the length of the fib sequences. It does not ask for subarray where elements have to be continuous. It is a strong indicator that it requires a 2D array, just like LIS.

- `base case`:
- `DP[i][j]`: length of longest fibonacci subsequence ending on `arr[i], arr[j]`
- `initialization`: 全部初始化2, 因为只要连成三个，2 + 1 = 3， 如果最后return的是2, 就说明没有找到任何fib-like sequence
- `transition function`:

Let'see an en example `arr = [1,2,3,4,5]`, 其实这是个sparse matrix, 由于限制条件 $arr[i]<arr[j]$, 初始化后如下表

|-|1|2|3|4|5|
|-|-|-|-|-|-|
|1|-|2|2|2|2|
|2|-|-|2|2|2|
|3|-|-|-|2|4|
|4|-|-|-|-|2|
|5|-|-|-|-|-|

这时候你需要update信息, 这时候你只需要找 $target = arr[j] - arr[i]$ 是否这个数组存在$arr[k] = target$ 且满足 $arr[k] < arr[i] < arr[j]$的规律即可

|-|1|2|3|4|5|
|-|-|-|-|-|-|
|1|-|2|2|2|2|
|2|-|-|3|2|2|
|3|-|-|-|3|4|
|4|-|-|-|-|1|
|5|-|-|-|-|-|

## Algorithm

## Code
```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # DP[i][j]: length of longest fibonacci subsequence ending on arr[i], arr[j]
        # for example: arr = [1,3,7,11,12,14,18], DP[3][4] = 3; [1,11,12] = [arr[0],arr[3],arr[4]]

        fib_hash = {}

        # create a hash for look up
        for i in range(len(arr)):
            fib_hash[arr[i]] = i
        
        # initialze 2D array
        DP = [[2 for _ in range(len(arr))] for _ in range(len(arr))]

        for j in range(len(arr)):
            for i in range(j):
                target = arr[j] - arr[i] # k增加,arr[k]增加,target单调递增
                # target < arr[i] < arr[j]
                if target < arr[i] and target in fib_hash:
                    k = fib_hash[target]
                    DP[i][j] = DP[k][i] + 1
        
        ans = max([max(value) for value in DP])

        return ans if ans >= 3 else 0
```