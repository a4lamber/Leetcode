---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Approach: bottom-up, linear space

## Brute force and intuition
The problem is asking for maxium score of any pair inside an array with constain `(i<j)`. The brute force would be searching any pair (1 + 2 + 3 + ... + n) $\approx O(n^2)$ and calculate score ($O(1)$). 

It is suggesting that the implemented DP solution won't be $O(n^2)$ like LIS that requires nested loop. So my thought process is to drop some unnecessary operations to minimize the time complexity. 
$$
\begin{align}
score &= \mathrm{values[i] + i + values[j] - j}\\
 &= f(i) + f(j)\\
\end{align}
$$
where $f(i)$ is a function of i and $f(j)$ is a function of j only.

Therefore, when we are traversing the array, the score of (i,j) depends on both i and j. But if we could keep track of the best index so far, we don't have to compare every single of index i < j.

> this idea is sort of like how `best sum` is equal to `best prefix sum` and `best postfix sum`

## Definion of DP

- `initialization`: all zeros or `float("-inf")` depending on the constrains given.
- `base case`: DP[0] = 0
- `DP[j]`: the maximum score one could get for the pair where it's (nums[i], nums[j])
- `state transition function`: with keeping tracking of best index, the current step `j` only depends one particular index `x` that gives the best condition but not depending on previous DP.
$$
\mathrm{DP[j] = values[j] + j - values[x] - x}
$$


```python
# O(n), O(n) solution
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # brute force would go through every single pair in the array, O(n^2)
        # DP[j]: the maximum score you could get for the pair where it's (nums[i], nums[j])

        if len(values) == 2: return values[1] + values[0] + 0 - 1

        # intiialze DP wizhe zeros
        DP = [0 for _ in range(len(values))]

        # find the prefix i that will give us highest score.
        best_prefix_i = 0
       

        for j in range(1,len(values)):
            if values[j-1] + j-1 >= values[best_prefix_i] + best_prefix_i:
                best_prefix_i = j-1
            DP[j] = best_prefix_i + values[best_prefix_i] + values[j] - j
        
        return max(DP)
```

with slight opimization, 
```python
# O(n), O(1) solution
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # brute force would go through every single pair in the array, O(n^2)

        if len(values) == 2: return values[1] + values[0] + 0 - 1

        # find the prefix i that will give us highest score.
        best_prefix_i = 0
        global_max = 0

        for j in range(1,len(values)):
            if values[j-1] + j-1 >= values[best_prefix_i] + best_prefix_i:
                best_prefix_i = j-1
            curr_max = best_prefix_i + values[best_prefix_i] + values[j] - j
            if curr_max > global_max: global_max = curr_max

        return global_max
```
