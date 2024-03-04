---
tags:
    - Array
    - Two Pointers
    - Greedy
    - Sorting
---

# 948 Bag of Tokens

The game rule is shown as follows:

- `face-up`: consume power worth `tokens[i]` but gain 1 score
- `face-down`: if you have at least 1 score, you can consume 1 score to gain `tokens[i]` power

You have an initial power of `power` and an initial score of 0. To maximum the score you get, you could play the game greedily by following the rules below:

- sort the tokens ascendingly
- if you have enough power to play cheapest token, play `face-up`
- if you don't have enough power but you do have score, play `face-down` on the most expensive token
- repeat until you can't play no more

You also need to maintain a variable to keep track of the maximum score you can get.

!!! note
    greedy works here because each subproblem is independent of each other and doesn't affect the overall result. 

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Yoooo! 
        # power >= tokens[i], 可以发动技能face-up. losing power for 1 score
        # score>= 1, you lost 1 score, but you gain tokens[i] power
        """
        我们可以做以下步骤
        1. sort them ascendingly and initialize two pointer, lo and hi
        2. play face-up when have enough power to increase score
        3. if we don't have enough power for step 2, and we do have >= 1 score, we play face down to gain power
        4. if we don't have power nor enough score, we can't play no more
        """
        tokens.sort()
        left,right = 0,len(tokens)-1
        score = 0
        best = 0
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
                best = max(best,score)
            elif score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        return best
```
