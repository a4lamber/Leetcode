---
tags:
    - Array
    - Linked List
    - Hash Table
---

# 3217 Delete Nodes From Linked List Present in Array

We have seen how to delete node from linked list. To generalized the operation of 

- delete head node
- delete interior node
- dead tail node


We can create a dummy header node to standardize the operation and generalize the unknown question to our known one.

Our train of thoughts are:

- create a hashset as a look up table
- traverse the linkedlist
    - if we find in lookup, delete the node
    - if we don't find it in lookup, just proceed

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. create a dummy header node such that it's same to delete any node in the linked list 
        """
        lookup = set(nums)
        dummy = ListNode(None,head)
        prev,curr = dummy,head

        while curr:
            if curr.val in lookup:
                temp = curr.next
                prev.next = temp
                curr.next = None
                # only advance the curr
                curr = temp
            else:
                # advance by one                
                prev = curr
                curr = curr.next

        return dummy.next
```