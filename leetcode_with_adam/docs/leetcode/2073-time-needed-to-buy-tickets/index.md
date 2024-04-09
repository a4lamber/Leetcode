---
tags:
    - Array
    - Queue
    - Simulation
---

# 2073 Time Needed to Buy Tickets

## Approach 1 One Pass

First round of intuition is that:

- if tickets[k] is min, then it's tickets[0] * n
- if tickets[k] is max, then it's sum(tickets)
- if tickets[k] is in between min and max of the array, there are some tricks can be done

Or more precisely:

- for tickets[i] strictly smaller than tickets[k], take tickets[i]
- for tickets[i] strictly larger than tickets[k], take the tickets[k]
- for tickets[i] == tickets[k], take either tickets[k] or tickets[i]
    
But one exception is that for the elements comes after the k, then we won't be going over them again,

```
            [         ]
[84,49,5,24,70,77,87,8]
         k
```

What's gonna happens is here if `tickets[i] >= tickets[k] and i > k`, we will decrement the total by 1.

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        if tickets[k] is min, then it's tickets[0] * n
        if tickets[k] is max, then it's sum(tickets)
        if in between min and max of the array, do some tricks:
            - for tickets[i] stricktly smaller than tickets[k], take tickets[i]
            - for tickets[i] stricktly larger than tickets[k], take the tickets[k]
            - for tickets[i] == tickets[k], take either
        then we also need to count the "last loop"
                    [         ]
        [84,49,5,24,70,77,87,8]
                 k
        the ones in the brackets, should minimize one
        """
        total = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                total += tickets[i]               
            else:
                total += tickets[k]
                if i > k:
                    total -= 1
                
        return total
```