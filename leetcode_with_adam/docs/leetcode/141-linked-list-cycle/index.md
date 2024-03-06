---
tags:
  - Linked List
  - Hash Table
  - Two Pointers
---


# [141 Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06)

> Follow up: can you solve it using O(1) (i.e. constant) memory?

## Approach 1: Floyd's turtle and hare

Classic cycle detection problem in linked list, could be solved by floyd's turtle and hare. 

Floyd's turtle and hare falls in the category of

- two pointers, 
- same direction
- two pointers moving at different speed (default is double)

!!! tip "[Floyd's Turtle and Hare](https://en.wikipedia.org/wiki/Cycle_detection)"
    是一种通用解for cycle detection in linked list. 用两个指针，一个快一个慢，如果有cycle，快的总会追上慢的.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head: return False
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
```