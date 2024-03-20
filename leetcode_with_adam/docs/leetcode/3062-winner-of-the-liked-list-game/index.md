---
tags:
    - Linked List
---

# [3062 Winner of the Linked List Game](https://leetcode.com/problems/winner-of-the-linked-list-game/description/?envType=weekly-question&envId=2024-03-01)

## Approach 1 Traverse

Just simply traverse it and you are good to go.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        # traverse with a counter for score
        scores = {
            'Odd' : 0,
            'Even': 0
        }

        curr = head
        while curr:
            even_power = curr.val
            curr = curr.next
            odd_power = curr.val
            if even_power > odd_power:
                scores['Even'] += 1
            elif even_power < odd_power:
                scores['Odd'] += 1
            
            curr = curr.next
        
        if scores['Even'] == scores['Odd']:
            return 'Tie'
        elif scores['Even'] > scores['Odd']:
            return 'Even'
        else:
            return 'Odd'
```
