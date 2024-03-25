---
tags:
    - Math
    - Simulation
---


# 2739 Total Distance Traveled

## Approach 1 O(n)

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total = 0
        used_in_main = 0
        while mainTank > 0:
            mainTank -= 1
            total += 10
            used_in_main += 1
            # check if we can refill or not
            if used_in_main %5 == 0:
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1            
        return total
```

## Approach 2 O(1) lee

Lee真的牛, solution [here](https://leetcode.com/problems/total-distance-traveled/solutions/3650469/java-c-python-math-o-1).

假设我们有mainTank (M) = 13, additionalTank (A) = 3.

我们总共能跑的数量可以分为两部分:

- mainTank自带的, $M$
- 由于我们跑的好，additionalTank补充的, x = f(M,A)

难点在于怎么判定f(M,A)的关系式.

```
M  M  M  M  M   A  M  M  M  M   A   M  M  M  M   A
1 [2  3  4  5]  6 [7  8  9 10]  11 [12 13 14 15] 16
```

我们在simulate的时候，mainTank的第一升油要作为`pseudo-oil-from-additional-tank`, 这样，你就在`M-1`中寻找，最多能组成几个`4`的倍数. 因此，我们可以得到:

$$
\begin{aligned}
x &= f(M,A) = min(\frac{M-1}{4}, A) \\
\text{total} &= (M + x) * 10
\end{aligned}
$$

where x is the number of additionalTank we can use, and total is the total distance we can travel.



```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank-1)//4, additionalTank)) * 10
```