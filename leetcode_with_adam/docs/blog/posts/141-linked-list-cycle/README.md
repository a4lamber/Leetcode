---
draft: true
date: 2023-11-13
authors:
  - adam
categories:
  - python
---

# Floyd's turtle and hare

Classic cycle detection problem in linked list, could be solved by floyd's turtle and hare. 

Floyd's turtle and hare falls in the category of
- two pointers, 
- same direction
- two pointers moving at different speed (default is double)



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