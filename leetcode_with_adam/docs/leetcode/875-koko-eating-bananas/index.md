---
tags:
    - Array
    - Binary Search
---
# [875 Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=binary-search)

??? tip "最大收获!"
    这题我学到最大的是, 重点在于更新条件的设定, 如下.
    ```python
    if hours <= h:
        # koko need to eat slower (less aggressive)
        right = mid
    else:
        # koko should eat faster
        left = mid + 1
    ```
    所有hours <= h的情况，koko都能吃完，所以在这里更新条件可以less aggressive, 说不定答案就在边界呢. 但对于hours > h的情况，koko就吃不完了，所以要更aggressive, 必须吃快点啊，mid是一定满足不了条件的.

## Approach 1 Binary Search

koko吃香蕉的速度，最慢是1，最快是max(piles), 之后再快也得等着，diminishing return. 之后我们可以用binary search来找到最小的k满足吃完香蕉的总时间不超过h. 我们所有的valid solution中，找到$k_{min}$ such that:

$$
\begin{align*}
\sum_{i=0}^{n-1} \lceil \frac{piles[i]}{k} \rceil \leq h \quad k \in \mathbb{Z}^{+}\\
\sum_{i=0}^{n-1} \lceil \frac{piles[i]}{k_{min}} \rceil = h \\
\end{align*}
$$



```python
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 由于diminishing return, 最快吃完是速度K = max(piles), 之后再快也得等着
        # 最慢速度为k = 1
        # 要求, 最小的k满足 sum([ceil(pile/k) for pile in piles]) == h
        # O(nlogn) + O(nlogn)
        
        # piles.sort()
        left,right = 1,max(piles)

        while left < right:
            mid = (left + right)//2
            hours = sum([math.ceil(pile/mid) for pile in piles])
            # print(f"{mid} {hours}")
            if hours <= h:
                # koko need to eat slower (less aggressive)
                right = mid
            else:
                # koko should eat faster
                left = mid + 1
                
        return left
```