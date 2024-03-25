---
tags:
    - Array
    - Greedy
    - Sorting
---


# 1710 Maximum Units on a Truck

贪心 + sorting的引入greedy的问题.

## Approach 1: Sort + Greedy

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        
        total = 0
        num_of_boxes = 0
        
        for boxes,units in boxTypes:
            if boxes + num_of_boxes > truckSize:
                remaining_space = truckSize - num_of_boxes
                total += remaining_space * units
                break
            # we can add it!
            total += boxes * units
            num_of_boxes += boxes
        
        return total
```

