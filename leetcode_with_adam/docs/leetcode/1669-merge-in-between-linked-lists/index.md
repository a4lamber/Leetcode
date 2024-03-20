---
tags:
    - Linked List
---

# [1669 Merge in Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/description/)


## Approach 1

Nothing fancy, just some traversal and pointer manipulation.

- Initialize two dummy header nodes
- Initialize `curr` and `prev` pointers for both list1 and list2
- Advancing both `prev` and `curr` in `list1`. Traverse such that `prev` is at the node before `a` and `curr` is at the node `a`
- Advancing only `curr` in `list1` it's at the next of node of b. If `b == 4`, `curr` is at the node 5
- Advancing `prev` and `curr` in `list2` until `curr` is at the end of list2
- connection time!!

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy1,dummy2 = ListNode(0,list1),ListNode(0,list2)
        curr1,curr2 = list1,list2
        prev1,prev2 = dummy1,dummy2

        counter = 0
        while counter < a and curr1:
            curr1 = curr1.next
            prev1 = prev1.next
            counter += 1
        
        # when we got here
        while counter <= b:
            curr1 = curr1.next
            counter += 1

        while curr2:
            prev2 = prev2.next
            curr2 = curr2.next
            
        # connect
        prev1.next = list2
        prev2.next = curr1
                
        return dummy1.next
```