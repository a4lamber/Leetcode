---
tags:
    - Two Pointers
    - Greedy
---

# 881 Boats to Save People

## Approach 1: Greedy

要找到最小数量的船来装所有的人，有两个constraints

- 一艘船最多只能装两个人
- 一艘船的最大载重是 `limit`

所以是一个有constraints的optimization问题，有两种可能性

- greedy
- dp

那么我们需要在每搜船中尽可能多的装人和尽可能多的重量，所以我们首先想到的是类似于高斯算法, 

```
1 2 3 4 5 6 7 8 9 10 = 55
```  

我们sort()之后，最重的人和最轻的人一起坐船，如果他们的重量小于等于limit，那么他们一起坐船，否则最重的人只能自己坐船。这个给予我们的思路是:

- 最重的人，如果和当前最轻的人一搜船都装不下，那么最重的人只能自己坐船.
- 最轻的人，如果都能和最重的人一起坐船，那么就能匹配所有人, 那还不如匹配最重的人.

!!! warning
    这题可以这样理解，排序之后，每一步寻找:

    - 当前最轻的人的最优解
        - `case 1:` 两人坐不下，当前最重的人的做进去
        - `case 2:` 两人坐得下，两人一起坐进去, 进入下一个解
    - 当前第二轻的人的最优解 (case 1) or 继续求解当前最轻的人的最优解 (case 1)
    - 重复上述步骤直到所有人都坐船
        


### Code Implementation

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        observation:
        - optimization problem, might be greedy. Each boat need 
        to fill as many people and as many weight as possible
        - sort之后two pointer, 如果lightest person和heavist person一起
        坐船，那么做; 如果不能，那最后heavist person只能自己做.
        """
        res = 0
        i,j = 0,len(people)-1
        people.sort()
        while i <= j:
            # lightest + heavist --> value
            if people[i] + people[j] <= limit:
                i += 1                
            # heavist person take your own boat
            j -= 1
            res += 1

        return res
```