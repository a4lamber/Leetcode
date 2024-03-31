# [3100 Water Bottles II](https://leetcode.com/problems/water-bottles-ii/description/)

Simulate the process of drinking water and exchanging bottles.

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        objective: find the maximum # of bottles you can drink
        observation:
        - objective = original bottles + bottles we exchange.
        - exchange rate goes high by 1 while we drinking it
        - 1 unit of exchange at a time
        algorithm:
        - initiazation we drink all the water
        - if we have enough empty bottles to exchange
            - full_bottles++, empty_bottles -= exchange_rate, exchange_rate += 1
            - until we don't have enough bottles
        - keeps exchanging 
        - not enough empty bottles, start to drink them all.
        - continue to exchange until 
        - drink them all
        """
        res = 0
        full_bottles = numBottles
        empty_bottles = 0
        exchange_rate = numExchange
        
        while full_bottles != 0:
            # drinking phase
            res += full_bottles
            empty_bottles += full_bottles        
            full_bottles = 0

            # exchange phase
            while empty_bottles >= exchange_rate:
                full_bottles += 1
                empty_bottles -= exchange_rate
                exchange_rate += 1

        return res
```